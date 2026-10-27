"""Artifact checks only: these do not execute the agent lifecycle."""
import hashlib
import json
from pathlib import Path
import re
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ['SKILL.md', 'reference/lifecycle.md', 'reference/records.md',
           'reference/customization.md', 'templates/facebook-posting/README.md',
           'templates/facebook-posting/validate.md', 'templates/facebook-posting/decision.md',
           'templates/facebook-posting/execute.md', 'templates/facebook-posting/report.md',
           'templates/facebook-posting/TOOLS.example.md']


def local_closure(root, entry):
    """Test utility for authored Markdown link closure, including symlinks."""
    root = root.resolve()
    pending, visited = [root / entry], set()
    while pending:
        path = pending.pop().resolve()
        if not path.is_relative_to(root):
            raise ValueError('external-instruction-dependency')
        if path in visited:
            continue
        if not path.is_file():
            raise ValueError('missing-local-resource')
        visited.add(path)
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
            target = link.split('#', 1)[0]
            if not target:
                continue
            if '://' in target or target.startswith('skill:'):
                raise ValueError('external-instruction-dependency')
            pending.append(path.parent / target)
    return visited


class PackageTests(unittest.TestCase):
    def test_current_release_is_bound_to_application_evidence(self):
        manifest = ROOT / 'tests/evidence/offline-release-binding.json'
        self.assertTrue(manifest.is_file(), 'Current release is not bound to application evidence')
        identities = json.loads(manifest.read_text())
        self.assertEqual(set(RUNTIME), set(identities))
        for name, digest in identities.items():
            self.assertEqual(digest, hashlib.sha256((ROOT / name).read_bytes()).hexdigest(),
                             'Runtime guidance changed: refresh affected offline applications')

    def test_required_runtime_artifacts_exist(self):
        self.assertEqual([], [p for p in RUNTIME if not (ROOT / p).is_file()],
                         'Self-contained runtime package is incomplete')

    def test_actual_local_instruction_closure(self):
        self.assertTrue((ROOT / 'SKILL.md').is_file(), 'Skill entrypoint absent')
        closure = local_closure(ROOT, 'SKILL.md')
        self.assertEqual(set(RUNTIME), {str(p.relative_to(ROOT)) for p in closure})
        self.assertFalse(any('specs' in p.parts for p in closure))

    def test_dependency_checker_rejects_missing_file(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'SKILL.md').write_text('[missing](absent.md)')
            with self.assertRaisesRegex(ValueError, 'missing-local-resource'):
                local_closure(root, 'SKILL.md')

    def test_dependency_checker_rejects_escaping_symlink(self):
        with tempfile.TemporaryDirectory() as folder:
            outer = Path(folder)
            root = outer / 'package'
            root.mkdir()
            (outer / 'outside.md').write_text('external instructions')
            (root / 'alias.md').symlink_to(outer / 'outside.md')
            (root / 'SKILL.md').write_text('[alias](alias.md)')
            with self.assertRaisesRegex(ValueError, 'external-instruction-dependency'):
                local_closure(root, 'SKILL.md')

    def test_instruction_identity_changes_with_contents(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / 'instruction.md'
            p.write_text('version one')
            bound = hashlib.sha256(p.read_bytes()).hexdigest()
            p.write_text('version two')
            self.assertNotEqual(bound, hashlib.sha256(p.read_bytes()).hexdigest())

    def test_generic_files_have_no_service_or_provider_defaults(self):
        for name in ['SKILL.md', 'reference/lifecycle.md', 'reference/records.md']:
            self.assertTrue((ROOT / name).is_file(), name)
            text = (ROOT / name).read_text().lower()
            for forbidden in ['@', 'smtp.', 'imap.', 'https://', '/home/', '/opt/']:
                self.assertNotIn(forbidden, text, name)

    def test_fixture_inventory_covers_approved_scenarios(self):
        fixture = json.loads((ROOT / 'tests/fixtures/scenarios.json').read_text())
        actual = {c['id'] for c in fixture}
        source = (ROOT / 'specs/changes/0001-service-executor/spec-delta.md').read_text()
        expected, req = set(), None
        for line in source.splitlines():
            match = re.match(r'### (REQ-EXEC-\d+) ', line)
            if match:
                req = match[1]
            match = re.match(r'\| ([SNB]\d+) \|', line)
            if match:
                expected.add(req + '.' + match[1])
        self.assertEqual(expected, actual)
        self.assertEqual(44, len(actual))


if __name__ == '__main__':
    unittest.main()
