"""Test-only Linux access observation; no executor policy or workflow logic.
Run with target-file, audit-output. Type STOP on stdin after the agent exits.
"""
import ctypes
import json
import os
from pathlib import Path
import select
import sys
import time

api=ctypes.CDLL(None,use_errno=True)
fd=api.inotify_init1(os.O_NONBLOCK)
if fd<0: raise OSError(ctypes.get_errno(),'inotify_init1')
target=Path(sys.argv[1]).resolve()
if api.inotify_add_watch(fd,os.fsencode(target),0x1|0x20)<0:
    raise OSError(ctypes.get_errno(),'inotify_add_watch')
start=time.time_ns(); events=[]
print('WATCH_READY',flush=True)
while True:
    ready,_,_=select.select([fd,sys.stdin],[],[])
    if fd in ready:
        events.append({'observed_ns':time.time_ns(),'kernel_event_bytes':os.read(fd,65536).hex()})
    if sys.stdin in ready and sys.stdin.readline().strip()=='STOP': break
Path(sys.argv[2]).write_text(json.dumps({'target':str(target),'started_ns':start,
    'stopped_ns':time.time_ns(),'events':events,'source':'Linux inotify IN_OPEN/IN_ACCESS'},indent=2)+'\n')
os.close(fd)
print('WATCH_STOPPED',len(events),flush=True)
