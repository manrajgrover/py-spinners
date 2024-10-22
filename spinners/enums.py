import itertools
from typing import Any

from spinners.base import *


class classproperty:
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, cls):
        return self.f(cls)


class EnumSpinners(BaseSpinners):
    """
    Wrapper class to register multiple Enum classes and access attributes from them.
    """

    def __getattr__(self, name):
        for enum in self._enums:
            try:
                return getattr(enum, name)
            except AttributeError:
                continue

    def __getitem__(self, name):
        for enum in self._enums:
            try:
                return enum[name]
            except KeyError:
                continue

        raise KeyError(name)

    @classproperty
    def _member_names_(self):
        return list(
            itertools.chain.from_iterable(enum._member_names_ for enum in self._enums)
        )

    @classproperty
    def _member_map_(self):
        return dict(
            itertools.chain.from_iterable(
                enum._member_map_.items() for enum in self._enums
            )
        )

    @classproperty
    def _value2member_map_(self):
        return dict(
            itertools.chain.from_iterable(
                enum._value2member_map_.items() for enum in self._enums
            )
        )

    @classproperty
    def _unhashable_values_(self):
        return list(
            itertools.chain.from_iterable(
                enum._unhashable_values_ for enum in self._enums
            )
        )


__all__ = [
    "EnumSpinners",
]
