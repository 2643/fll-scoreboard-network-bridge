#!/usr/bin/env python3
import os
import sys
import secrets
import string
import time
from subprocess import Popen, STDOUT, PIPE

# Get the path this file is in
path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), 'server.py')


correct = True
while True:
    try:
        p = Popen(['curl 192.168.1.55:81/scores.xml --output scores.xml'], shell=True)
        p.wait()
        p = Popen([sys.executable, '-u', path],
              stdout=PIPE, stdin=PIPE, encoding='utf-8')
        time.sleep(23)
        p.terminate()
        p.wait()
    except KeyboardInterrupt:
        sys.exit(0)