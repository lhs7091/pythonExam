import os
from tkinter import *
import tkinter.font as tkFont

print("Start Program")

root = Tk()
root.title("No Title - NotePad")
root.geometry("640x480")
filename="mynote.txt"

def open_file():
    print("Start Open function")
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf-8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())
    print("End Open function")


def save_file():
    print("Start Save function")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(txt.get("1.0", END))
    print("End Save function")


"""
Menu bar Area

"""
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_cascade()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

menu.add_cascade(label="Edit")
menu.add_cascade(label="Form")
menu.add_cascade(label="View")
menu.add_cascade(label="Help")

root.config(menu=menu)

"""
Text Area
"""
# Scroll Bar
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# text area
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)

root.mainloop()