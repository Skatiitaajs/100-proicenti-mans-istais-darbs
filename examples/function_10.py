"""
Funkcija: random.triangular()

Īss paskaidrojums:
`triangular(low, high, mode)` atgriež nejaušu decimālskaitli.
Rezultāts biežāk būs tuvumā vērtībai `mode`, nevis vienādi sadalīts
visā intervālā.
"""

import random
import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def run_example():
    print("Funkcija: random.triangular()")
    print("Paskaidrojums: rezultāts biežāk atrodas tuvāk tipiskajai vērtībai.")

    random.seed(14)

    # Piemērs: skolēna ceļš uz skolu parasti ilgst ap 20 minūtēm,
    # bet dažreiz var būt no 10 līdz 40 minūtēm.
    travel_time = random.triangular(10, 40, 20)

    print("Aptuvenais ceļa laiks uz skolu:", round(travel_time, 1), "minūtes")


if __name__ == "__main__":
    run_example()
