"""
Funkcija: random.gauss()

Īss paskaidrojums:
`gauss(mu, sigma)` ģenerē skaitli pēc normālā jeb Gausa sadalījuma.
`mu` ir vidējā vērtība, bet `sigma` parāda, cik ļoti rezultāti parasti
atšķiras no vidējās vērtības.
"""

import random
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def run_example():
    print("Funkcija: random.gauss()")
    print("Paskaidrojums: ģenerē vērtību ap noteiktu vidējo lielumu.")

    random.seed(11)

    # Piemērs: pārbaudes darba vērtējums ap 7 ballēm.
    grade = random.gauss(7, 1.5)

    print("Ģenerētais vērtējums:", round(grade, 1))


if __name__ == "__main__":
    run_example()
