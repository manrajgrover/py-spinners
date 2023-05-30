from enum import Enum


Spinners = Enum('Spinners', {
    "dots": {
        "interval": 80,
        "frames": [
            "⠋",
            "⠙",
            "⠹",
            "⠸",
            "⠼",
            "⠴",
            "⠦",
            "⠧",
            "⠇",
            "⠏"
        ]
    },
    "dots2": {
        "interval": 80,
        "frames": [
            "⣾",
            "⣽",
            "⣻",
            "⢿",
            "⡿",
            "⣟",
            "⣯",
            "⣷"
        ]
    }
})

print([x for x in dir(Spinners) if "__" not in x])
print(Spinners['dots'].value['frames'])
