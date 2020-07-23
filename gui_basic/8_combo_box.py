from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk

root = Tk()
root.title("Combo Box")
root.geometry("640x480")
fontStyle = tkFont.Font(size=20)

values = [str(i) + "일" for i in range(1,32)]
combobox = ttk.Combobox(root, height=5, values=values, state="readonly")
combobox.pack()
combobox.set("card payment day")

def btncmd():
    print(combobox.get())
    pass


btn = Button(root, text="Select", command=btncmd)
btn.pack()

root.mainloop()