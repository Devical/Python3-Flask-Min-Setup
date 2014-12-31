#! /usr/bin/python3

import sys

activate_this = '/var/www/signingacademy/venv/bin/activate_this.py'

with open(activate_this) as f:
    code = compile(f.read(), activate_this, 'exec')
    exec(code, dict(__file__=activate_this))

sys.stdout = sys.stderr
sys.path.insert(0, 'var/www/signingacademy')

from app import app as application
