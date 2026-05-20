"""
Funkcija: random.normalvariate()

Īss paskaidrojums:
`normalvariate(mu, sigma)` arī ģenerē skaitli pēc normālā sadalījuma.
Praktiski to var izmantot līdzīgi kā gauss(), piemēram, simulācijām.
"""

import random
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def run_example():
    print("Funkcija: random.normalvariate()")
    print("Paskaidrojums: ģenerē nejaušu vērtību ap vidējo vērtību.")

    random.seed(17)

    # Piemērs: skolēna auguma simulācija centimetros.
    height = random.normalvariate(170, 8)

    print("Ģenerētais augums:", round(height, 1), "cm")


if __name__ == "__main__":
    run_example()
