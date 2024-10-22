import re
import subprocess


def get_codepage(default: str = None) -> str:
    """Get the encoding of the systems terminal."""

    try:
        result = subprocess.run(
            ["cmd.exe", "/c", "chcp"],
            text=True,
            capture_output=True,
            check=True,
        )

        cp = re.search(r"\d{3,5}", result.stdout).group(0)
    except (subprocess.CalledProcessError, AttributeError):
        return default or "utf-8"

    return f"cp{cp}"


__all__ = [
    "get_codepage",
]
