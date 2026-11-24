"""One-Line Roast: The Gadget You Use Every Day.

Writes the single roast line to /output/entry.txt.
Standard library only.
"""

import os

ROAST = (
    "My charger only works if I hold the cable at a 37-degree angle. "
    "It's not a charger, it's a trust exercise."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ROAST)


if __name__ == "__main__":
    main()
