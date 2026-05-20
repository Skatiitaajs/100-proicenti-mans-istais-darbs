"""
Funkcija: random.getrandbits()

Īss paskaidrojums:
`getrandbits(k)` izveido nejaušu veselu skaitli ar k bitiem.
Piemēram, 8 biti var veidot skaitli no 0 līdz 255.
"""

import random
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def run_example():
    print("Funkcija: random.getrandbits()")
    print("Paskaidrojums: izveido nejaušu veselu skaitli no noteikta bitu skaita.")

    random.seed(18)

    # Izveidojam 8 bitu skaitli.
    number = random.getrandbits(8)

    # format(number, "08b") parāda skaitli binārā pierakstā ar 8 cipariem.
    binary_number = format(number, "08b")

    print("Nejaušs 8 bitu skaitlis:", number)
    print("Binārais pieraksts:", binary_number)


if __name__ == "__main__":
    run_example()
