"""
Funkcija: random.uniform()

Īss paskaidrojums:
`uniform(a, b)` atgriež nejaušu decimālskaitli starp a un b.
To var izmantot, ja vajag nejaušu temperatūru, cenu vai attālumu.
"""

import random
import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def run_example():
    print("Funkcija: random.uniform()")
    print("Paskaidrojums: iegūst nejaušu decimālskaitli starp divām robežām.")

    random.seed(9)

    # Izveidojam nejaušu klases telpas temperatūru.
    temperature = random.uniform(18.0, 24.0)

    print("Nejauša temperatūra klasē:", round(temperature, 1), "°C")


if __name__ == "__main__":
    run_example()
