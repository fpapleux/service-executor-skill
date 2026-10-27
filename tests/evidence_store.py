"""Extract retained synthetic evidence with standard tarfile; no agent execution.

For manual inspection: python3 tests/evidence_store.py /path/to/empty-folder
"""
import atexit
from functools import lru_cache
from pathlib import Path
import sys
import tarfile
import tempfile

ARCHIVE = Path(__file__).resolve().parent / 'evidence/offline-artifacts.tar.gz'


def extract(destination):
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    with tarfile.open(ARCHIVE, 'r:gz') as archive:
        archive.extractall(destination, filter='data')
    return destination


@lru_cache(maxsize=1)
def evidence_root():
    temporary = tempfile.TemporaryDirectory(prefix='service-executor-evidence-')
    atexit.register(temporary.cleanup)
    return extract(temporary.name)


if __name__ == '__main__':
    extract(sys.argv[1])
