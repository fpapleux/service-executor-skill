"""Check the test double itself without implementing an executor."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from offline_native import call


class NativeDoubleTests(unittest.TestCase):
    def test_native_response_does_not_make_workflow_decisions(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'native.json').write_text(json.dumps({'post': {'status': 'accepted'}}))
            with contextlib.redirect_stdout(io.StringIO()):
                call(root, 'post', {'caption': 'exact', 'page': 'PAGE-A'})
                call(root, 'comment', {})
            calls = [json.loads(s) for s in (root / 'native-calls.jsonl').read_text().splitlines()]
            self.assertEqual(['post', 'comment'], [c['operation'] for c in calls])
            self.assertEqual('exact', json.loads((root / 'effects/post.json').read_text())['caption'])
            self.assertFalse((root / 'journal.jsonl').exists())
            self.assertFalse((root / 'locks').exists())
