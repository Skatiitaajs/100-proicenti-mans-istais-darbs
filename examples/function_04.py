"""
Funkcija: random.randrange()

Īss paskaidrojums:
`randrange(start, stop, step)` izvēlas nejaušu skaitli no range().
Atšķirībā no randint(), beigu robeža `stop` nav iekļauta.
"""

import random
import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def run_example():
    print("Funkcija: random.randrange()")
    print("Paskaidrojums: izvēlas skaitli no noteikta range() intervāla.")

    random.seed(8)

    # Izvēlamies nejaušu pāra skaitli no 0 līdz 20.
    # 22 nav iekļauts, bet 20 var tikt izvēlēts.
    even_number = random.randrange(0, 22, 2)

    print("Nejaušs pāra skaitlis no 0 līdz 20:", even_number)


if __name__ == "__main__":
    run_example()
