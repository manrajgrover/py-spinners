import sys


def main():
    """
    spinners from `cli-spinners` are loaded on startup directly from the json file

    https://github.com/sindresorhus/cli-spinners/blob/main/spinners.json
    """
    from spinners import Spinners

    available = Spinners.available

    print(f"{len(available)} available spinners from 'cli-spinners'")
    print(available, end="\n\n")

    guaranteed = Spinners.guaranteed

    print(
        f"{len(guaranteed)} guaranteed '{Spinners.codepage()}' spinners for your {sys.platform=}"
    )
    print(guaranteed, end="\n\n")


if __name__ == "__main__":
    main()
