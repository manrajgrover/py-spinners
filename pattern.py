"""
Python wrapper for beautiful terminal spinner library by @sindresorhus.

https://github.com/sindresorhus/cli-spinners
"""
from __future__ import unicode_literals

from enum import Enum
import json
import os
from constants import CLI_SPINNERS_DIR, SPINNER_FILE

"""
Read the spinners from cli-spinner submodule
"""
with open(os.path.join(CLI_SPINNERS_DIR, SPINNER_FILE)) as data:
    spinners = json.load(data)

Patterns = Enum('Patterns', spinners)
