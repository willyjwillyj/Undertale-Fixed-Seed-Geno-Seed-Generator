import tkinter as tk
import rngGen as rngGen
import requests
import webbrowser  
from tkinter.filedialog import asksaveasfile

root = tk.Tk()
root.title("Undertale Fixed Seed Geno Seed Generator")
root.geometry("400x100")

def genBoard():
    rngGen.genProcess()
    

current_version = "v1.0.0"
github_connection_success = False
newest_version = current_version

try:
    release_data = requests.get("https://github.com/willyjwillyj/Undertale-Fixed-Seed-Geno-Seed-Generator")
    newest_version = (release_data.json()["name"])
except:
    pass
else:
    github_connection_success = True
    

ver_label = tk.Label(master=root, text="You are using version " + current_version)
ver_label.grid(row=0,column=0)

if github_connection_success:
    if newest_version == current_version:
        ver_label_success = tk.Label(master=root, text="You are on the latest version")
        ver_label_success.grid(row=0,column=1)
    else:
        ver_label_failure = tk.Button(master=root, text="Update to the latest version", command=lambda:webbrowser.open("https://github.com/willyjwillyj/Undertale-Fixed-Seed-Geno-Seed-Generator", new=0, autoraise=True))
        ver_label_failure.grid(row=0,column=1)
else:
    ver_label_failure = tk.Label(master=root, text="Failed to discover latest version")
    ver_label_failure.grid(row=0,column=1)



genButton = tk.Button(master=root, text="Generate Seed", command=genBoard)

genButton.grid(row=1,column=0)


root.mainloop()