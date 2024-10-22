import enum

import pytest

from spinners.errors import *
from spinners.future import *


@pytest.fixture
def _Spinners():
    spin = enum.Enum(
        "TestSpinners",
        {
            "line": {"interval": 100, "frames": ["-", "\\", "|", "/"]},
            "triangle": {"interval": 50, "frames": ["◢", "◣", "◤", "◥"]},
        },
    )

    Spinners._enums.clear()

    Spinners.append(spin)

    yield Spinners()

    Spinners._enums.clear()


@pytest.fixture
def FutureSpinner():
    Spinners._enums.clear()

    yield Spinners

    Spinners._enums.clear()


@pytest.mark.parametrize(
    "cp, result",
    [
        ("cp850", ["line"]),
        ("utf-8", ["line", "triangle"]),
        (None, ["line", "triangle"]),
    ],
)
def test_spinners(_Spinners, cp, result):

    assert _Spinners.spinners(cp) == result


def test_spinners_available(_Spinners):

    assert list(spinners_available()).sort() == ["line", "triangle"].sort()


def test_spinners_guaranteed(_Spinners):

    spin = spinners_guaranteed()

    assert len(spin) > 0


def test_spinners_validation(_Spinners, invalid_spinner):

    with pytest.raises(ValidationSpinnerError):
        _Spinners.append(invalid_spinner)


def test_load(_Spinners):
    _Spinners.load_spinners()

    assert 2 < len(_Spinners.guaranteed) <= len(_Spinners.available)


def test_load_raises(_Spinners):
    with pytest.raises(FileNotFoundError):
        _Spinners.load_spinners("nonexistent.json")


def test_unique(FutureSpinner, spinners):

    FutureSpinner.append(spinners)

    assert FutureSpinner(unique=True)


def test_unique_raies(FutureSpinner, spinners):

    FutureSpinner.append(spinners)
    FutureSpinner.append(spinners)

    with pytest.raises(DuplicateSpinnerError):
        FutureSpinner(unique=True)


def test_duplicates(FutureSpinner, spinners):

    FutureSpinner.append(spinners)
    FutureSpinner.append(spinners)

    assert FutureSpinner().spinners().sort() == ["line", "dots"].sort()


def test_subclass(FutureSpinner):

    class AsciiSpinner(FutureSpinner):
        dots = {"interval": 80, "frames": [".  ", ".. ", "...", "   "]}
        line = {"interval": 100, "frames": ["-", "\\", "|", "/"]}

    class UTFSpinner(FutureSpinner):
        smiley = {"interval": 200, "frames": ["😄 ", "😝 "]}

    assert FutureSpinner().spinners().sort() == ["dots", "line", "smiley"].sort()


def test_subclass_raises(FutureSpinner):

    with pytest.raises(ValidationSpinnerError) as e:

        class InvalidSpinner(FutureSpinner, strict=True):
            dots = {}


def test_subclass_strict(FutureSpinner):

    class InvalidSpinner(FutureSpinner, strict=False):
        pass

    assert FutureSpinner().spinners() == []


def test_subclass_unique(FutureSpinner):
    class AsciiSpinner(FutureSpinner, strict=True):
        dots = {"interval": 80, "frames": [".  ", ".. ", "...", "   "]}
        line = {"interval": 100, "frames": ["-", "\\", "|", "/"]}

    with pytest.raises(DuplicateSpinnerError):

        class UTFSpinner(FutureSpinner, strict=True):
            dots = {
                "interval": 80,
                "frames": ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"],
            }
