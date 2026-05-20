"""
Funkcija: random.choice()

Īss paskaidrojums:
`choice(sequence)` izvēlas vienu nejaušu elementu no saraksta,
teksta virknes vai citas secības.
"""

import random
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def run_example():
    print("Funkcija: random.choice()")
    print("Paskaidrojums: izvēlas vienu nejaušu elementu no saraksta.")

    random.seed(12)

    students = ["Anna", "Jānis", "Marta", "Rihards"]

    # Izvēlamies vienu skolēnu, piemēram, prezentācijas sākšanai.
    chosen_student = random.choice(students)

    print("Saraksts:", students)
    print("Izvēlētais skolēns:", chosen_student)


if __name__ == "__main__":
    run_example()
