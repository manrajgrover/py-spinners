import pytest

from spinners.base import *
from spinners.errors import *


@pytest.mark.parametrize(
    "attr",
    [
        "insert",
        "append",
        "_validate_enum",
    ],
)
def test_base_callables(attr):

    func = getattr(BaseSpinners, attr)

    assert callable(func)


def test_append_invalid_class(classes, invalid_class):
    with pytest.raises(ValidationError):
        classes.append(invalid_class)


def test_append(classes, spinners):
    classes.append(spinners)

    assert spinners in classes._enums


@pytest.mark.parametrize(
    "index",
    [
        0,
        float(-1),
    ],
)
def test_insert_invalid_class(classes, invalid_class, index):
    with pytest.raises(ValidationError):
        classes.insert(index, invalid_class)


def test_insert_invalid_index(classes, spinners):
    with pytest.raises(TypeError):
        classes.insert(float(-1), spinners)


def test_insert(classes, spinners):
    classes.insert(0, spinners)

    assert spinners in classes._enums
