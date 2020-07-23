from tkinter import *
import tkinter.font as tkFont

root = Tk()
root.title("Radio Button")
root.geometry("640x480")
fontStyle = tkFont.Font(size=20)

Label(root, text="select menu", font=fontStyle).pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="hamburger", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="chease-hamburger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="chicken-hamburger", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="select drink", font=fontStyle).pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="coke", value="coke", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="cider", value="cider", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get())
    print(drink_var.get())
    pass


btn = Button(root, text="Order", command=btncmd)
btn.pack()

root.mainloop()