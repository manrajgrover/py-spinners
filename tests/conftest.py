import enum
from typing import Any, Dict, Generator, Type

import pytest

from spinners.base import BaseSpinners
from spinners.enums import EnumSpinners
from spinners.future import Spinners


@pytest.fixture(
    params=[
        BaseSpinners,
        EnumSpinners,
        Spinners,
    ],
    ids=lambda cls: cls.__name__,
)
def classes(request) -> Generator[Type[Any], None, None]:
    cls = request.param

    cls._enums.clear()

    yield cls

    cls._enums.clear()


@pytest.fixture
def obj_spinners() -> Dict[str, Dict[str, Any]]:
    return {
        "line": {
            "interval": 100,
            "frames": [
                "-",
                "\\",
                "|",
                "/",
            ],
        },
        "dots": {
            "interval": 80,
            "frames": [
                ".  ",
                ".. ",
                "...",
                "   ",
            ],
        },
    }


@pytest.fixture
def spinners(obj_spinners) -> enum.Enum:
    return enum.Enum(
        "spinner",
        obj_spinners,
    )


@pytest.fixture(
    params=[
        {"none": None},
        {"line": {"interval": 0, "frames": ["-", "\\", "|", "/"]}},
        {"dots": {"interval": 80, "frame": [".  ", ".. ", "...", "   "]}},
        {"empty": {"interval": 100, "frames": []}},
        {"nolist": {"interval": 100, "frames": None}},
        {"nostr": {"interval": 100, "frames": [".", 1, "...", "   "]}},
        {"baloon": {"interval": "1", "frames": [".", "o", "O", "°"]}},
    ],
    ids=lambda e: list(e.keys())[0],
)
def obj_invalid_spinners(request) -> Dict[str, Dict[str, Any]]:
    return request.param


@pytest.fixture
def invalid_spinner(obj_invalid_spinners) -> enum.Enum:
    return enum.Enum(
        "invalid_spinner",
        obj_invalid_spinners,
    )


@pytest.fixture(
    params=[list, dict, set],
)
def invalid_class(request) -> Type[Any]:
    return request.param
