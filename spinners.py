"""
Python wrapper for beautiful terminal spinner library by @sindresorhus.

https://github.com/sindresorhus/cli-spinners

Attributes
----------
CURR_DIR : str
    Current directory path
Spinners : Enum
    Spinners for command line spinners
"""
from __future__ import unicode_literals

from enum import Enum
import json
import os
from constants import CLI_SPINNERS_DIR, SPINNER_FILE

CURR_DIR = os.path.dirname(__file__)

"""
Read the spinners from cli-spinner submodule
"""
with open(os.path.join(CURR_DIR, CLI_SPINNERS_DIR, SPINNER_FILE)) as data:
    spinners = json.load(data)

Spinners = Enum('Spinners', spinners)
