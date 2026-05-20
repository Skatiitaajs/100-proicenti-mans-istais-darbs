"""
Funkcija: random.randint()

Īss paskaidrojums:
`randint(a, b)` atgriež nejaušu veselu skaitli no a līdz b.
Abas robežas ir iekļautas, piemēram, randint(1, 6) var dot arī 1 un 6.
"""

import random
import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def run_example():
    print("Funkcija: random.randint()")
    print("Paskaidrojums: iegūst nejaušu veselu skaitli starp divām robežām.")

    random.seed(3)

    # Šis piemērs imitē metamā kauliņa mešanu.
    dice_result = random.randint(1, 6)

    print("Metamā kauliņa rezultāts:", dice_result)


if __name__ == "__main__":
    run_example()
