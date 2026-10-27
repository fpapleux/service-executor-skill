"""Offline test double for explicit native calls. No executor decisions/locks/retries.

Usage: python3 tests/offline_native.py CASE_DIR OPERATION JSON_PARAMETERS
Every call is logged, including prohibited/unsupported operations. Responses are
fixture data. Only export/post/report create their corresponding synthetic effect.
"""
import json
import fcntl
from pathlib import Path
import sys
import time


def call(root, operation, parameters):
    root = Path(root)
    config = json.loads((root / 'native.json').read_text())
    journals = {}
    for path in (root / 'state/requests').glob('*/journal.jsonl'):
        try:
            journals[str(path.relative_to(root))] = path.read_text()
        except (OSError, UnicodeError) as exc:
            journals[str(path.relative_to(root))] = {'read_error': type(exc).__name__}
    locks = {}
    for path in (root / 'state/locks').glob('*.lock'):
        with path.open('a') as handle:
            try:
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
                locks[path.name] = 'available'
                fcntl.flock(handle, fcntl.LOCK_UN)
            except BlockingIOError:
                locks[path.name] = 'held'
    log = root / 'native-calls.jsonl'
    with log.open('a') as stream:
        stream.write(json.dumps({'operation': operation, 'parameters': parameters,
                                 'observed_ns': time.time_ns(), 'journals_before': journals, 'locks_before': locks}) + '\n')
    response = config.get(operation, {'status': 'unsupported'})
    if response.get('status') == 'accepted':
        effects = root / 'effects'
        effects.mkdir(exist_ok=True)
        if operation == 'export':
            source = root / parameters['source']
            (effects / 'export.txt').write_bytes(source.read_bytes())
        elif operation == 'post':
            (effects / 'post.json').write_text(json.dumps(parameters))
        elif operation == 'report':
            with (effects / 'reports.jsonl').open('a') as stream:
                stream.write(json.dumps(parameters) + '\n')
    print(json.dumps(response))


if __name__ == '__main__':
    call(sys.argv[1], sys.argv[2], json.loads(sys.argv[3]))
