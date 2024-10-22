import enum


def main():
    """
    add new spinners using decorator, functions and inheritance
    """
    import spinners as sp
    from spinners import Spinners

    print(f"1. add a new spinner using the `register_spinner` decorator")

    @sp.register_spinner
    class CloudSpinner(enum.Enum):
        rain = {
            "interval": 1000,
            "frames": [
                "☁️",
                "🌧️",
                "⛈️",
            ],
        }

    print(Spinners.rain.value, end="\n\n")

    print("2. add a new spinner using the `register_spinner` function")

    smily = enum.Enum(
        "smily",
        {
            "smily": {
                "interval": 100,
                "frames": [
                    "😀",
                    "😁",
                    "😂",
                    "😃",
                ],
            }
        },
    )

    sp.register_spinner(smily)

    print(Spinners.smily.value, end="\n\n")

    print(
        "3. add a new spinner using inheritance, `strict` to check for a unique spinner name"
    )

    class SurfSpinner(sp.FutureSpinners, strict=True):
        wave = {
            "interval": 100,
            "frames": [
                "🌊",
                "🏄",
                "🌊",
            ],
        }

    print(Spinners.wave.value, end="\n\n")

    print("4. add a old LegacySpinners ontop 'cli-spinners'")
    try:
        Spinners.append(sp.LegacySpinners)
    except sp.ValidationSpinnerError as e:
        print(f"- {e}")
    else:
        print("- all spinners valid")

    try:
        Spinners.unique()
    except sp.DuplicateSpinnerError as e:
        print(f"- {e.message}")
    else:
        print("- no duplicate names found")


if __name__ == "__main__":
    main()
