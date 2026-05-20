"""
Galvenā programma manam `random` bibliotēkas projektam.

Programma parāda izvēlni. Lietotājs ievada piemēra numuru, un tiek
palaists attiecīgais fails no mapes `examples`.
"""

import sys

from examples import function_01
from examples import function_02
from examples import function_03
from examples import function_04
from examples import function_05
from examples import function_06
from examples import function_07
from examples import function_08
from examples import function_09
from examples import function_10
from examples import function_11
from examples import function_12
from examples import function_13
from examples import function_14
from examples import function_15


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


examples = [
    ("random.seed()", function_01.run_example),
    ("random.random()", function_02.run_example),
    ("random.randint()", function_03.run_example),
    ("random.randrange()", function_04.run_example),
    ("random.choice()", function_05.run_example),
    ("random.choices()", function_06.run_example),
    ("random.shuffle()", function_07.run_example),
    ("random.sample()", function_08.run_example),
    ("random.uniform()", function_09.run_example),
    ("random.triangular()", function_10.run_example),
    ("random.gauss()", function_11.run_example),
    ("random.normalvariate()", function_12.run_example),
    ("random.getrandbits()", function_13.run_example),
    ("random.randbytes()", function_14.run_example),
    ("random.betavariate()", function_15.run_example),
]


def show_menu():
    """Izdrukā visus pieejamos piemērus."""
    print("\n`random` bibliotēkas piemēri")
    print("-----------------------------")

    for number, example in enumerate(examples, start=1):
        function_name = example[0]
        print(f"{number}. {function_name}")

    print("0. Beigt programmu")


def main():
    """Ļauj lietotājam izvēlēties un palaist vienu piemēru."""
    while True:
        show_menu()
        choice = input("\nIevadi piemēra numuru: ")

        if choice == "0":
            print("Programma pabeigta.")
            break

        if not choice.isdigit():
            print("Lūdzu, ievadi skaitli no 0 līdz 15.")
            continue

        example_number = int(choice)

        if 1 <= example_number <= len(examples):
            print("\n--- Rezultāts ---")
            example_function = examples[example_number - 1][1]
            example_function()
        else:
            print("Tāda piemēra nav. Mēģini vēlreiz.")


if __name__ == "__main__":
    main()
