"""Validate reviewed exercise evidence; this suite does not call a model.

Re-run the documented synthetic agent exercises when instructions change.
A green result means retained, reviewed evidence matches the recorded package,
not that the current machine has executed a business service.
"""
import hashlib
import json
import os
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PHASE = os.environ.get('EXERCISE_PHASE', 'green')
CASES = json.loads((ROOT / 'tests/fixtures/scenarios.json').read_text())


class ReviewedExerciseTests(unittest.TestCase):
    pass


def case_test(case):
    def test(self):
        path = ROOT / 'tests/evidence' / f'{PHASE}-review.json'
        self.assertTrue(path.is_file(), 'No reviewed agent exercise is available')
        reviews = json.loads(path.read_text())
        matches = [r for r in reviews if r['id'] == case['id']]
        self.assertEqual(1, len(matches), 'Scenario lacks a unique review')
        review = matches[0]
        trace = ROOT / 'tests/evidence' / review['trace']
        self.assertTrue(trace.is_file())
        responses = json.loads(trace.read_text())
        response = [r for r in responses if r['id'] == case['id']]
        self.assertEqual(1, len(response), 'Review lacks an attributable response')
        self.assertTrue(response[0]['actions'])
        self.assertTrue(review['assessment'])
        self.assertTrue(review['passed'], review['assessment'])
        if PHASE == 'green':
            self.assertEqual(review['trace_sha256'], hashlib.sha256(trace.read_bytes()).hexdigest())
            manifest = json.loads((ROOT / 'tests/evidence/package-binding.json').read_text())
            for name, digest in manifest.items():
                self.assertEqual(digest, hashlib.sha256((ROOT / name).read_bytes()).hexdigest(),
                                 'Guidance changed: rerun controlled exercises')
    return test


for case in CASES:
    name = 'test_' + case['id'].replace('-', '_').replace('.', '_')
    setattr(ReviewedExerciseTests, name, case_test(case))


if __name__ == '__main__':
    unittest.main()
