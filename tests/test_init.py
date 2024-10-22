import enum

from spinners import Spinners
from spinners.future import Spinners as FutureSpinners
from spinners.spinners import Spinners as LegacySpinners


def test_spinners():
    assert isinstance(Spinners, FutureSpinners)


def test_legacy():
    assert issubclass(LegacySpinners, enum.Enum)


def test_future():
    assert issubclass(FutureSpinners, object)
