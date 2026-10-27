"""Assertions over actual offline agent artifacts and native test-double calls."""
import json
from datetime import datetime
from pathlib import Path
import unittest
from evidence_store import evidence_root

ROOT = Path(__file__).resolve().parents[1]


class OfflineApplicationTests(unittest.TestCase):
    def test_REQ_EXEC_001_S1_actual_export(self):
        case = evidence_root() / 'offline/REQ-EXEC-001.S1'
        original = json.loads((case / 'original.json').read_text())
        self.assertEqual('source.txt', original['source'])
        effect = case / 'effects/export.txt'
        self.assertTrue(effect.is_file(), 'Authorized export did not produce its actual offline effect')
        self.assertEqual((case / 'source.txt').read_bytes(), effect.read_bytes())
        calls = [json.loads(s) for s in (case / 'native-calls.jsonl').read_text().splitlines()]
        ops = [c['operation'] for c in calls]
        self.assertEqual(1, ops.count('export'))
        self.assertTrue(all(op in {'inspect', 'export', 'report'} for op in ops))
        report = [c['parameters'] for c in calls if c['operation'] == 'report']
        self.assertTrue(any(r['request_id'] == 'R1' and r['outcome'] == 'completed' for r in report))
        journals = list((case / 'state/requests').glob('*/journal.jsonl'))
        self.assertEqual(1, len(journals))
        events = [json.loads(s) for s in journals[0].read_text().splitlines()]
        stages = [e['stage'] for e in events]
        self.assertIn('validate', stages)
        acceptance = [i for i,e in enumerate(events) if e.get('outcome') == 'accepted']
        self.assertTrue(acceptance, 'No affirmative acceptance was recorded')
        intents = [i for i,e in enumerate(events) if e.get('event') == 'intent' and e['stage'] == 'execute']
        self.assertTrue(intents, 'No persisted business intent')
        self.assertLess(stages.index('validate'), acceptance[0])
        self.assertLess(acceptance[0], intents[0])
        submitted = next(c for c in calls if c['operation'] == 'export')
        self.assertLess(datetime.fromisoformat(events[intents[0]]['observed_at']).timestamp(), submitted['observed_ns'] / 1e9)
        self.assertTrue(any(e['stage'] == 'execute' and e['outcome'] == 'completed' for e in events))
        self.assertTrue(any(e['stage'] == 'report' and e['outcome'] == 'submitted' for e in events))
        request = journals[0].parent / 'request.md'
        self.assertTrue(request.is_file())
        self.assertIn('source.txt', request.read_text())
