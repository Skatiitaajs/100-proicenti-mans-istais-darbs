"""
Funkcija: random.shuffle()

Īss paskaidrojums:
`shuffle(list)` nejauši samaina saraksta elementu secību.
Svarīgi: funkcija maina esošo sarakstu, nevis izveido jaunu sarakstu.
"""

import random
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def run_example():
    print("Funkcija: random.shuffle()")
    print("Paskaidrojums: sajauc saraksta elementus nejaušā secībā.")

    random.seed(21)

    cards = ["A", "K", "Q", "J", "10"]
    print("Sākotnējais saraksts:", cards)

    # Sajaucam kāršu sarakstu.
    random.shuffle(cards)

    print("Sajauktais saraksts:", cards)


if __name__ == "__main__":
    run_example()
