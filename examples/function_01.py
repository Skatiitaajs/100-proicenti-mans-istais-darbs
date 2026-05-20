"""
Funkcija: random.seed()

Īss paskaidrojums:
`seed()` iestata nejaušo skaitļu ģeneratora sākuma vērtību.
Ja izmanto vienādu sākuma vērtību, Python izveido vienādu nejaušo
skaitļu secību. Tas ir noderīgi, ja gribam piemēru atkārtot un pārbaudīt.
"""

import random
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def run_example():
    print("Funkcija: random.seed()")
    print("Paskaidrojums: vienāda seed vērtība dod vienādu rezultātu secību.")

    # Iestatām sākuma vērtību 25.
    random.seed(25)

    # Izveidojam divus nejaušus veselus skaitļus.
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)

    # Vēlreiz iestatām to pašu sākuma vērtību.
    # Tāpēc nākamie divi skaitļi būs tādi paši kā iepriekš.
    random.seed(25)
    repeated_first_number = random.randint(1, 100)
    repeated_second_number = random.randint(1, 100)

    print("Pirmā secība:", first_number, second_number)
    print("Atkārtotā secība:", repeated_first_number, repeated_second_number)


if __name__ == "__main__":
    run_example()
