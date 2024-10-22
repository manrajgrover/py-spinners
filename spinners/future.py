import enum
import json
import sys
from pathlib import Path
from typing import List, Set

from spinners.codepage import *
from spinners.enums import *
from spinners.errors import *

if sys.version_info < (3, 9):
    import importlib_resources as pkg_resources
else:
    import importlib.resources as pkg_resources


class Spinners(EnumSpinners):

    def __init__(self, *, unique: bool = False):

        if unique is True:
            self.unique()

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__()

        check = kwargs.get("strict", False)
        index = kwargs.get("priority", -1)

        try:
            data = {
                k: v
                for k, v in cls.__dict__.items()
                if not k.startswith("__") and isinstance(v, dict)
            }

            cls.insert(index, enum.Enum(cls.__name__, data))

            if check:
                cls.unique()
        except ValidationError as e:
            if check:
                raise e

    @classmethod
    def unique(cls) -> bool:
        seen = set()
        duplicates = [
            name
            for name in cls._member_names_  # pylint: disable=E1133
            if name in seen or seen.add(name)
        ]
        if duplicates:
            raise DuplicateSpinnerError(duplicates)

        return True

    @classmethod
    def _validate_enum(cls, obj: enum.Enum) -> bool:
        valid = super()._validate_enum(obj)

        try:
            for spinner in obj._member_map_.keys():
                spin = getattr(obj, spinner).value

                if not isinstance(spin, dict):
                    raise ValidationSpinnerError(f"{spin=} must be of type 'dict'")

                interval = spin["interval"]

                if not isinstance(interval, int) or interval <= 0:
                    raise ValidationSpinnerError(
                        f"{interval=} must be of type 'int' and greater than 0"
                    )

                frames = spin["frames"]

                if not isinstance(frames, list):
                    raise ValidationSpinnerError(f"{frames=} must be of type 'list'")

                if not len(frames):
                    raise ValidationSpinnerError(f"{frames=} must not be empty")

                for frame in frames:
                    if not isinstance(frame, str):
                        raise ValidationSpinnerError(f"{frame=} must be of type 'str'")

        except KeyError as e:
            raise ValidationSpinnerError(
                f"{str(e)} must be a key in '{obj.__name__}'"
            ) from e

        return valid and True

    def spinners(self, codepage: str = None) -> List[str]:

        enums = self._member_map_.keys()

        if codepage is None:
            return list(enums)

        def encoder(self):
            for enum in enums:
                spin = getattr(self, enum).value

                try:
                    for frame in spin["frames"]:
                        frame.encode(codepage)
                except UnicodeEncodeError as e:
                    continue

                yield enum

        return list(encoder(self))

    @classmethod
    def codepage(cls) -> str:
        return get_codepage()

    @classmethod
    def load_spinners(cls, jsonfile: str = None, **kwargs):

        if jsonfile is None:
            jsonfile = pkg_resources.files("spinners").joinpath(
                "../cli-spinners/spinners.json"
            )

        content = Path(jsonfile).read_text(encoding=kwargs.get("encoding", "utf-8"))

        cls.insert(
            kwargs.get("priority", 0),
            enum.Enum(
                jsonfile.resolve().as_posix(),
                json.loads(content),
            ),
        )

        return cls()

    @property
    def available(self) -> Set[str]:
        return set(self.spinners())

    @property
    def guaranteed(self) -> Set[str]:
        return set(self.spinners(self.codepage()))


def spinners_guaranteed() -> Set[str]:
    spin = Spinners()
    cp = spin.codepage()

    return set(spin.spinners(cp))


def spinners_available() -> Set[str]:
    return set(Spinners().spinners(None))


__all__ = [
    "Spinners",
    "spinners_guaranteed",
    "spinners_available",
]
