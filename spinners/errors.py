from typing import List


class ValidationError(TypeError):
    pass


class ValidationSpinnerError(ValidationError):
    pass


class ValidationObjectError(ValidationError):
    pass


class DuplicateSpinnerError(ValidationError):

    def __init__(self, duplicates: List[str]):
        """
        Raised when registered spinner names are not unique.
        """
        self.message = f"Spinners are not unique: {len(duplicates)} {duplicates=}"
        self.duplicates = duplicates
        super().__init__(self.message)


__all__ = [
    "ValidationError",
    "ValidationSpinnerError",
    "ValidationObjectError",
    "DuplicateSpinnerError",
]
