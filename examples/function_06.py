"""
Funkcija: random.choices()

Īss paskaidrojums:
`choices(population, weights, k)` izvēlas vairākus elementus.
Atšķirībā no sample(), viens un tas pats elements var atkārtoties.
Ar `weights` var noteikt, kuri elementi parādās biežāk.
"""

import random
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def run_example():
    print("Funkcija: random.choices()")
    print("Paskaidrojums: izvēlas vairākus elementus ar atkārtošanos.")

    random.seed(15)

    prizes = ["mazā balva", "vidējā balva", "lielā balva"]
    weights = [70, 25, 5]

    # Lielāks svars nozīmē lielāku iespēju, ka elements tiks izvēlēts.
    selected_prizes = random.choices(prizes, weights=weights, k=5)

    print("Iespējamās balvas:", prizes)
    print("Izlozes rezultāti:", selected_prizes)


if __name__ == "__main__":
    run_example()
