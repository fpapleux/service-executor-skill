"""Exercise the existing OS lock primitive, not an executor implementation."""
import fcntl
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


class OwnershipPrimitiveTests(unittest.TestCase):
    def test_two_processes_cannot_own_same_stable_lock(self):
        with tempfile.TemporaryDirectory() as folder:
            lock = Path(folder) / 'shared.lock'
            with lock.open('a') as handle:
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
                child = 'import fcntl,sys; f=open(sys.argv[1],"a"); fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)'
                result = subprocess.run([sys.executable, '-c', child, str(lock)], capture_output=True)
                self.assertNotEqual(0, result.returncode)
                self.assertIn(b'BlockingIOError', result.stderr)
                other = Path(folder) / 'independent.lock'
                independent = subprocess.run([sys.executable, '-c', child, str(other)], capture_output=True)
                self.assertEqual(0, independent.returncode, independent.stderr)
            released = subprocess.run([sys.executable, '-c', child, str(lock)], capture_output=True)
            self.assertEqual(0, released.returncode, released.stderr)


if __name__ == '__main__':
    unittest.main()
