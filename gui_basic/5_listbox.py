from tkinter import *

root = Tk()
root.title("List Box")
root.geometry("640x480")


listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "water melon")
listbox.pack()

def btncmd():
    # listbox.delete(END) # delete last one
    # listbox.delete(0) # delete first one
    print("Lists : ", listbox.size())

    # listbox.get(start index, end index)
    print("from first to third : ", listbox.get(0,2))

    # selection check, return index number
    print("selected content : ", listbox.curselection())


btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()