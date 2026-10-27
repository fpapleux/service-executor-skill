"""Observe executor-created files/calls, never manufacture a passing exercise.

Fixture setup is explicit: python3 tests/offline_fixture.py. Tests never reset it.
The agent must actually run each case; missing observations are failures.
"""
import hashlib
import fcntl
from datetime import datetime
import json
from pathlib import Path
import unittest
from evidence_store import evidence_root

ROOT = Path(__file__).resolve().parents[1]
BASE = evidence_root() / 'offline'


def lines(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()] if path.is_file() else []


class OfflineRemaining(unittest.TestCase):
    def artifacts(self, sid):
        case = (evidence_root()/'offline-retest'/sid) if sid=='REQ-EXEC-004.S1' else (evidence_root()/'offline-read-audit'/sid) if sid=='REQ-EXEC-002.N3' else BASE/sid
        self.assertTrue((case / 'case.json').is_file(), 'Incomplete Given fixture')
        for name, expected in json.loads((case / 'immutable.json').read_text()).items():
            self.assertEqual(expected, hashlib.sha256((case / name).read_bytes()).hexdigest(),
                             'Immutable original/binding/configuration changed: ' + name)
        journals = list((case / 'state/requests').glob('*/journal.jsonl'))
        events = [e for path in journals for e in lines(path)]
        prior = case / 'prior-journal.jsonl'
        if prior.exists():
            self.assertTrue((case / 'state/requests/R1/journal.jsonl').read_text().startswith(prior.read_text()),
                            'Prior journal history rewritten')
        calls = lines(case / 'native-calls.jsonl')
        observed = [e for e in events if not str(e.get('event_id','')).startswith('seed-')]
        reply = (case / 'reply.txt').read_text() if (case / 'reply.txt').is_file() else ''
        self.assertTrue(observed or reply, 'No actual executor observation/result')
        return case, events, observed, calls, reply

    def check(self, sid):
        case, events, observed, calls, reply = self.artifacts(sid)
        short = sid.removeprefix('REQ-EXEC-')
        original = json.loads((case / 'original.json').read_text())
        ops = [c['operation'] for c in calls]
        self.assertTrue(set(ops) <= {'inspect','export','post','report','reconcile'},
                        'Unexpected native operation or follow-up')
        reports = [c['parameters'] for c in calls if c['operation']=='report']
        for call in calls:
            if call['operation'] not in {'export','post'}:
                continue
            snapshots = call.get('journals_before', {})
            before = [json.loads(line) for text in snapshots.values() if isinstance(text,str)
                      for line in text.splitlines() if line.strip()]
            self.assertTrue(any(e.get('event') in {'accepted','acceptance'} or
                                e.get('outcome')=='accepted' for e in before),
                            'No persisted affirmative acceptance before effect')
            self.assertTrue(any(e.get('event')=='intent' for e in before),
                            'No persisted intent before effect')
            self.assertEqual('held',call.get('locks_before',{}).get('request-R1.lock'),
                             'Request kernel lock not held during effect')
            self.assertEqual('held',call.get('locks_before',{}).get('resource-shared.lock'),
                             'Shared-resource kernel lock not held during effect')
        new_text = json.dumps(observed).lower() + reply.lower()
        report_text = json.dumps(reports).lower() + reply.lower()
        errors = {
            '001.N2':'acceptance-required',
            '002.N1':'incomplete-service-definition','002.N3':'external-instruction-dependency',
            '002.N4':'conflicting-service-definition','003.N1':'request-not-found',
            '003.N2':'instruction-version-mismatch','003.N3':'record-unavailable',
            '004.N1':'resource-unresolved','004.N3':'ownership-unavailable',
            '005.N1':'missing-report-configuration','006.N3':'missing-customization-resource'}
        no_effect = set(errors) | {'001.N1','004.N4','004.N5','005.S2','005.N2','005.N3',
                                  '006.N1','006.N2','007.N1','007.N2','007.N3','007.N5','007.N6'}
        if short=='001.N1':
            self.assertIn('source',report_text)
            self.assertTrue(any(word in report_text for word in ['missing','absent','required']))
        if short in errors:
            self.assertIn(errors[short], new_text)
            self.assertIn(errors[short], report_text, 'Failure not communicated through authorized route')
        if short in no_effect:
            self.assertNotIn('export',ops)
            self.assertNotIn('post',ops)
            self.assertFalse((case/'effects/export.txt').exists())
            self.assertFalse((case/'effects/post.json').exists())
        if short in {'001.N1','007.N1'}:
            self.assertIn('reject',new_text)
        if short == '001.N3':
            self.assertEqual(1,ops.count('export'))
            self.assertFalse((case/'effects/export.txt').exists())
            self.assertIn('failed',new_text)
            self.assertTrue(any(r.get('outcome')=='failed' for r in reports))
        if short == '001.B1':
            self.assertEqual(1,ops.count('export'))
            self.assertEqual((case/'source.txt').read_bytes(),(case/'effects/export.txt').read_bytes())
            self.assertTrue(reply,'Session reply absent')
            self.assertNotIn('post',ops)
        if short in {'002.S1','003.B1','004.S1','005.S3'}:
            self.assertEqual(1,ops.count('export'))
            self.assertEqual((case/'source.txt').read_bytes(),(case/'effects/export.txt').read_bytes())
        if short in {'002.S1','003.B1'}:
            bindings=list((case/'state/requests').glob('*/binding/**/*'))
            self.assertTrue(any(p.is_file() for p in bindings),'No bound instruction closure')
            identities='\n'.join(p.read_text(errors='replace') for p in bindings if p.is_file())
            self.assertIn('synthetic-reference-only',identities)
            for name in ['validate.md','decision.md','execute.md','report.md','config.json']:
                self.assertIn(name,identities,'Missing closure identity '+name)
        if short=='002.N2':
            self.assertNotIn('new-template',json.dumps(observed))
            self.assertNotIn('export',ops,'Completed action replayed')
        if short=='002.N3':
            audit=json.loads((case/'access-audit.json').read_text())
            self.assertEqual([],audit['events'],'External instruction target was opened or read')
            self.assertLess(audit['started_ns'],calls[0]['observed_ns'])
            self.assertGreater(audit['stopped_ns'],calls[-1]['observed_ns'])
        if short=='002.N5':
            self.assertEqual(1,ops.count('export'))
            self.assertEqual((case/'source.txt').read_bytes(),(case/'effects/export.txt').read_bytes())
            self.assertNotIn('outside-skill.md',[str(p) for p in (case/'state').rglob('*')])
        if short=='003.S1':
            exports=[c for c in calls if c['operation']=='export']
            self.assertEqual(1,len(exports))
            self.assertEqual('source-b.txt',exports[0]['parameters']['source'])
            self.assertEqual((case/'source-b.txt').read_bytes(),(case/'effects/export.txt').read_bytes())
            self.assertTrue(any(e.get('stage')=='validate' for e in observed),'Pending B not revalidated')
        if short=='003.N1':
            self.assertFalse((case/'state/requests').exists(),'Replacement request allocated')
        if short=='003.N3':
            self.assertIn('state/requests',report_text)
            self.assertTrue(any(word in report_text for word in ['write','append','persist','mkdir','creat']))
        if short=='004.S1':
            self.assertTrue(any(e.get('event')=='intent' and e.get('owner_token') for e in observed))
            releases=[e for e in observed if e.get('event')=='release']
            self.assertTrue(releases,'No durable release record')
            closeout=releases[-1]
            self.assertTrue(closeout['resources_being_released'])
            self.assertTrue(closeout['owner_token'])
            completion=closeout['operation_completion_evidence']
            self.assertEqual(0,completion['native_export_returncode'])
            self.assertTrue(completion['evidence'])
            for field in ['unresolved_effects','replay_holds','dependency_holds','pending_communication']:
                self.assertEqual([],closeout[field])
            self.assertTrue(closeout['next_action'])
            close_at=datetime.fromisoformat(closeout['observed_at']).timestamp()
            self.assertGreater(close_at,max(c['observed_ns'] for c in calls)/1e9)
            for lock in (case/'state/locks').glob('*.lock'):
                with lock.open('a') as handle:
                    fcntl.flock(handle,fcntl.LOCK_EX|fcntl.LOCK_NB)
                    fcntl.flock(handle,fcntl.LOCK_UN)
        if short in {'004.N2','004.N6'}:
            proof=case/'concurrency.json'
            self.assertTrue(proof.is_file(),'Real two-agent contention observation absent')
            proof=json.loads(proof.read_text())
            self.assertEqual({'A','B'},set(proof['sessions']))
            raw=lines(case/'raw-lock-observations.jsonl')
            self.assertTrue(raw,'No observed kernel-lock acquisition/contention/release trace')
            def instant(session,event):
                aliases={'lock-acquired':{'lock-acquired','acquired'},'lock-contended':{'lock-contended','contention'},'lock-released':{'lock-released','released'}}
                matches=[r['observed_ns'] for r in raw if r.get('session')==session and r.get('event') in aliases[event]]
                self.assertTrue(matches,session+' '+event+' absent')
                return min(matches)
            acquired=instant('A','lock-acquired')
            contended=instant('B','lock-contended')
            released=instant('A','lock-released')
            self.assertLess(acquired,contended)
            self.assertLess(contended,released)
            business=[c for c in calls if c['operation'] in {'export','post'}]
            self.assertEqual(1,len(business),'Expected exactly one owner effect during contention')
            self.assertLess(acquired,business[0]['observed_ns'])
            self.assertLess(business[0]['observed_ns'],released)
            contention=[r for r in raw if r.get('session')=='B' and r.get('event') in {'lock-contended','contention'}]
            self.assertTrue(any(r.get('exception_type')=='BlockingIOError' or r.get('errno')==11 for r in contention),'No native kernel failure observation')
            for item in raw:
                trace=case/item.get('trace','raw-'+item['session']+'.txt')
                self.assertTrue(trace.is_file(),'Kernel observation lacks raw tool trace')
                self.assertIn(str(item['pid']),trace.read_text(),'Actor PID absent from raw process trace')
            owner_events=[e for e in observed if e.get('stage')=='execute' and e.get('outcome') in {'completed','submitted'}]
            self.assertTrue(owner_events)
            self.assertEqual(1,len({e['owner_token'] for e in owner_events}))
            if short=='004.N6':
                self.assertFalse(any(e.get('owner_token')=='B' for e in observed),'Loser wrote shared request')
            else:
                for path in (case/'state/requests').glob('*/journal.jsonl'):
                    self.assertTrue(all(e.get('request_id')==path.parent.name for e in lines(path)),
                                    'Cross-request journal write')
            for path in proof['evidence']:
                self.assertTrue((case/path).is_file(),'Raw concurrent tool trace absent')
        if short=='004.N3':
            self.assertEqual(b'\xff',(case/'state/locks/resource-shared.owner.json').read_bytes(),'Unreadable ownership evidence replaced')
        if short=='004.N4':
            self.assertIn('reconcile',ops)
            self.assertTrue(any(c['parameters'].get('attempt_id')=='A1' for c in calls if c['operation']=='reconcile'))
            self.assertIn('unknown',new_text)
            self.assertIn('hold',new_text)
        if short=='004.N5':
            self.assertIn('stale',new_text)
            self.assertEqual({'owner':'B','token':'current-B'},json.loads((case/'state/locks/request-R1.owner.json').read_text()))
            self.assertEqual((case/'prior-journal.jsonl').read_text(),(case/'state/requests/R1/journal.jsonl').read_text())
        if short in {'005.S1','007.S3'}:
            self.assertTrue(reports)
            receipts=[p for p in (case/'state/requests').glob('*/evidence/*.json')]
            self.assertTrue(any('portal-R1' in p.read_text() for p in receipts),'Native receipt evidence missing')
            self.assertFalse(any(r.get('delivered') is True or r.get('read') is True for r in reports),
                             'Unsupported delivery/read claim')
        if short=='005.S3':
            self.assertLess(ops.index('report'),ops.index('export'),'Outage was not encountered before continuing export')
        if short=='005.S2':
            self.assertTrue(reports)
            payload=reports[0]
            for field in ['request_id','reason','confirmed_effects','required_intervention']:
                self.assertIn(field,payload)
            self.assertIn('blocked',new_text)
        if short in {'005.S3','007.N4'}:
            self.assertTrue(reports)
            self.assertIn('pending',new_text)
            self.assertTrue(reply,'Available requester route did not surface reporting gap')
            self.assertNotIn('rejected',new_text)
        if short=='005.N2':
            self.assertNotIn('report',ops,'Confirmed incident report duplicated')
            self.assertIn('failed',new_text)
        if short=='005.N3':
            self.assertIn('reconcile',ops)
            self.assertTrue(any(c['parameters'].get('attempt_id')=='N1' for c in calls if c['operation']=='reconcile'))
            self.assertNotIn('report',ops,'Unknown report blindly resent')
            self.assertIn('unknown',new_text)
        if short=='005.N4':
            self.assertNotIn('export',ops)
            self.assertNotIn('post',ops)
            self.assertEqual(1,ops.count('report'))
            self.assertEqual('I1',reports[0]['incident_id'],'Reporting obligation identity changed')
            self.assertTrue(any(e.get('stage')=='report' and e.get('outcome')=='submitted' for e in observed))
        if short=='006.S1':
            template=case/'created-template'
            for name in ['README.md','validate.md','decision.md','execute.md','report.md','TOOLS.md']:
                self.assertTrue((template/name).is_file(),'Actual operator template absent: '+name)
            content=' '.join(p.read_text() for p in template.glob('*.md')).lower()
            self.assertIn('document',content)
            self.assertIn('portal',content)
            execute=(template/'execute.md').read_text().lower()
            self.assertIn('export',execute)
            self.assertNotIn('native post',execute)
            self.assertNotIn('native comment',execute)
            self.assertNotIn('facebook-posting/',content)
        if short=='006.N1':
            self.assertIn('incomplete',new_text)
            self.assertIn('decision',new_text)
            self.assertNotIn('ready-for-execution',new_text.replace('not ready-for-execution',''))
        if short=='006.N2':
            changes=list((case/'operator-changes').glob('*'))
            self.assertTrue(changes,'No separate attributable change request')
            text=' '.join(p.read_text() for p in changes if p.is_file())
            self.assertIn('R1',text)
            self.assertTrue(any(w in text.lower() for w in ['evidence','problem']))
        if short.startswith('007.'):
            if short=='007.N4':
                self.assertNotIn('post',ops,'Confirmed post replayed during report-only continuation')
                self.assertTrue((case/'effects/post.json').is_file())
            if short in {'007.S1','007.S2','007.S3','007.B1'}:
                self.assertEqual(1,ops.count('post'))
                post=json.loads((case/'effects/post.json').read_text())
                for field in ['page_id','caption','image','placement','timing']:
                    self.assertEqual(original[field],post[field],field+' changed')
                self.assertTrue(set(post)<= {'page_id','caption','image','placement','timing','request_id','attempt_id'})
                self.assertIn('native-post-r1',new_text)
            if short=='007.N4':
                self.assertNotIn('post',ops,'Confirmed post replayed during report-only continuation')
                self.assertTrue((case/'effects/post.json').is_file())
            if short in {'007.S1','007.S2','007.S3','007.B1'}:
                self.assertIn('inspect',ops)
                self.assertTrue(reports)
            if short=='007.N1': self.assertIn('caption',report_text)
            if short=='007.N2':
                self.assertIn('identity',new_text)
                self.assertIn('mismatch',new_text)
            if short=='007.N3':
                self.assertTrue(reports)
                self.assertIn('permission',report_text)
                self.assertIn('blocked',new_text)
            if short=='007.N5':
                self.assertIn('past',report_text)
                self.assertTrue(reports)
            if short=='007.N6':
                self.assertIn('schedul',report_text)
                self.assertIn('blocked',new_text)


def install(sid):
    def test(self): self.check(sid)
    test.__name__='test_'+sid.replace('-','_').replace('.','_')
    setattr(OfflineRemaining,test.__name__,test)


for row in json.loads((ROOT/'tests/fixtures/scenarios.json').read_text()):
    if row['id']!='REQ-EXEC-001.S1': install(row['id'])
