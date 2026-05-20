"""
Funkcija: random.sample()

Īss paskaidrojums:
`sample(population, k)` izvēlas k unikālus elementus no saraksta.
Tas nozīmē, ka viens un tas pats elements netiek izvēlēts divreiz.
"""

import random
import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def run_example():
    print("Funkcija: random.sample()")
    print("Paskaidrojums: izvēlas vairākus unikālus elementus bez atkārtošanās.")

    random.seed(30)

    participants = ["Anna", "Jānis", "Marta", "Rihards", "Elīna", "Tomass"]

    # Izvēlamies trīs uzvarētājus no dalībnieku saraksta.
    winners = random.sample(participants, k=3)

    print("Dalībnieki:", participants)
    print("Uzvarētāji:", winners)


if __name__ == "__main__":
    run_example()
