"""Fuehrt find_single_element auf einer gegebenen Eingabe aus.

Aufruf:
    python run_single.py 1 2 3 4 3 1 2
    -> Einzelnes Element: 4
"""

import sys

from single_element import find_single_element


def main(args: list[str]) -> None:
    if not args:
        print("Aufruf: python run_single.py <int> <int> ...")
        sys.exit(1)

    try:
        numbers = [int(arg) for arg in args]
    except ValueError:
        print("Fehler: alle Argumente muessen Integer sein.")
        sys.exit(1)

    result = find_single_element(numbers)
    print(f"Eingabe: {numbers}")
    print(f"Einzelnes Element: {result}")


if __name__ == "__main__":
    main(sys.argv[1:])