"""
Vizuālā programma Python bibliotēkas `random` izpētes projektam.

Šis fails izmanto `tkinter`, kas arī ir Python standarta bibliotēkā.
Programma ļauj izvēlēties piemēru sarakstā un palaist to ar pogu.
"""

import contextlib
import io
import tkinter as tk
from tkinter import ttk

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


examples = [
    ("1. random.seed()", function_01.run_example),
    ("2. random.random()", function_02.run_example),
    ("3. random.randint()", function_03.run_example),
    ("4. random.randrange()", function_04.run_example),
    ("5. random.choice()", function_05.run_example),
    ("6. random.choices()", function_06.run_example),
    ("7. random.shuffle()", function_07.run_example),
    ("8. random.sample()", function_08.run_example),
    ("9. random.uniform()", function_09.run_example),
    ("10. random.triangular()", function_10.run_example),
    ("11. random.gauss()", function_11.run_example),
    ("12. random.normalvariate()", function_12.run_example),
    ("13. random.getrandbits()", function_13.run_example),
    ("14. random.randbytes()", function_14.run_example),
    ("15. random.betavariate()", function_15.run_example),
]


def run_selected_example():
    """Palaiž izvēlēto piemēru un parāda rezultātu teksta laukā."""
    selected_index = example_list.current()

    if selected_index == -1:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Lūdzu, vispirms izvēlies piemēru.")
        return

    example_function = examples[selected_index][1]

    # Piemēru faili izmanto print(), tāpēc šeit īslaicīgi saglabājam izdruku.
    text_buffer = io.StringIO()
    with contextlib.redirect_stdout(text_buffer):
        example_function()

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, text_buffer.getvalue())


root = tk.Tk()
root.title("Python random bibliotēkas piemēri")
root.geometry("720x460")

title_label = ttk.Label(
    root,
    text="Python standarta bibliotēka random",
    font=("Segoe UI", 16, "bold"),
)
title_label.pack(pady=12)

description_label = ttk.Label(
    root,
    text="Izvēlies funkciju un palaid piemēru.",
    font=("Segoe UI", 10),
)
description_label.pack()

example_names = []
for example in examples:
    example_names.append(example[0])

example_list = ttk.Combobox(root, values=example_names, state="readonly", width=35)
example_list.pack(pady=10)
example_list.current(0)

run_button = ttk.Button(root, text="Palaist piemēru", command=run_selected_example)
run_button.pack(pady=5)

output_text = tk.Text(root, height=14, width=78, wrap="word")
output_text.pack(padx=16, pady=12, fill="both", expand=True)

root.mainloop()
