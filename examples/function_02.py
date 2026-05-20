"""
Funkcija: random.random()

Īss paskaidrojums:
`random()` atgriež nejaušu decimālskaitli no 0.0 līdz 1.0.
Skaitlis var būt 0.0, bet tas nevar būt tieši 1.0.
"""

import random
import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def run_example():
    print("Funkcija: random.random()")
    print("Paskaidrojums: iegūst nejaušu decimālskaitli intervālā [0.0, 1.0).")

    # Seed padara piemēru atkārtojamu.
    random.seed(10)

    # Ģenerējam nejaušu decimālskaitli.
    random_number = random.random()

    # round() izmantojam tikai tāpēc, lai rezultāts būtu īsāks.
    print("Nejaušais skaitlis:", round(random_number, 4))


if __name__ == "__main__":
    run_example()
