import random
from tkinter import filedialog

def genProcess():
    text = ""
    for i in range(50000):
        text += str(random.randint(0,9999))
        text += "\n"
    f = filedialog.asksaveasfile("w",initialfile=("rngData"))
    f.write(text)