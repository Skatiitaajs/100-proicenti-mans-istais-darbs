"""
Funkcija: random.betavariate()

Īss paskaidrojums:
`betavariate(alpha, beta)` atgriež skaitli no 0 līdz 1.
To var izmantot proporciju vai procentu simulācijām.
"""

import random
import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def run_example():
    print("Funkcija: random.betavariate()")
    print("Paskaidrojums: ģenerē proporciju intervālā no 0 līdz 1.")

    random.seed(22)

    # Piemērs: simulējam, kāda daļa no uzdevuma jau ir izpildīta.
    progress = random.betavariate(2, 5)
    progress_percent = progress * 100

    print("Simulētais darba progress:", round(progress_percent, 1), "%")


if __name__ == "__main__":
    run_example()
