import enum

import pytest

from spinners.register import *


def test_register(classes):

    assert not classes._enums

    @register_spinner
    class TestDot(enum.Enum):
        dot = {"interval": 80, "frames": [".  ", ".. ", "...", "   "]}

    assert TestDot in classes._enums


def test_register_prio_none(classes):

    assert not classes._enums

    @register_spinner()
    class TestDot(enum.Enum):
        dot = {"interval": 80, "frames": [".  ", ".. ", "...", "   "]}

    assert TestDot in classes._enums


def test_register_prio_one(classes):

    assert not classes._enums

    @register_spinner(priority=1)
    class TestDot(enum.Enum):
        dot = {"interval": 80, "frames": [".  ", ".. ", "...", "   "]}

    assert TestDot in classes._enums


def test_register_priority(classes):

    assert not classes._enums

    @register_spinner()
    class TestDot(enum.Enum):
        dot = {"interval": 80, "frames": [".  ", ".. ", "...", "   "]}

    @register_spinner(priority=-1)
    class TestLine(enum.Enum):
        line = {"interval": 100, "frames": ["-", "\\", "|", "/"]}

    assert classes._enums[0] == TestLine
    assert classes._enums[1] == TestDot


def test_register_noenum():

    with pytest.raises(ValidationError):

        @register_spinner
        class TestClass:
            dot = {"interval": 80, "frames": [".  ", ".. ", "...", "   "]}
