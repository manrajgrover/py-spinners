from spinners.errors import *
from spinners.future import Spinners as FutureSpinners
from spinners.register import register_spinner
from spinners.spinners import Spinners as LegacySpinners

Spinners = FutureSpinners.load_spinners()


__all__ = [
    "FutureSpinners",
    "LegacySpinners",
    "Spinners",
    "register_spinner",
    "ValidationError",
    "ValidationSpinnerError",
    "DuplicateSpinnerError",
]
