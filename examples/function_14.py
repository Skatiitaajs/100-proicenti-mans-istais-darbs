"""
Funkcija: random.randbytes()

Īss paskaidrojums:
`randbytes(n)` izveido n nejaušus baitus.
Šī funkcija var noderēt demonstrācijām, bet drošības nolūkiem
labāk izmantot `secrets` bibliotēku.
"""

import random
import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def run_example():
    print("Funkcija: random.randbytes()")
    print("Paskaidrojums: izveido noteiktu skaitu nejaušu baitu.")

    random.seed(19)

    # Izveidojam 4 nejaušus baitus.
    random_bytes = random.randbytes(4)

    # .hex() parāda baitus ērtāk lasāmā sešpadsmitnieku formā.
    print("Nejaušie baiti:", random_bytes)
    print("HEX pieraksts:", random_bytes.hex())


if __name__ == "__main__":
    run_example()
