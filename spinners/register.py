from enum import Enum

from spinners.base import BaseSpinners, ValidationError


def register_spinner(cls=None, /, *, priority=-1):

    def wrap(cls):
        try:
            BaseSpinners.insert(priority, cls)
        except ValidationError as e:
            raise ValidationError(f"{cls} is not a suitable spinner") from e

        return cls

    # See if we're being called as @register_spinner or @register_spinner().
    if cls is None:
        # We're called with parens.
        return wrap

    # We're called as @register_spinner without parens.
    return wrap(cls)


__all__ = [
    "Enum",
    "register_spinner",
    "ValidationError",
]
