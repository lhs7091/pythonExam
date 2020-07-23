from tkinter import *

root = Tk()
root.title("Frame")
root.geometry("640x480")

Label(root, text="Select Menu").pack(side="top")

Button(root, text="order").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="hamburger").pack()
Button(frame_burger, text="chease burger").pack()
Button(frame_burger, text="chicken burger").pack()

frame_drink = LabelFrame(root, text="drink")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="coke").pack()
Button(frame_drink, text="cider").pack()

root.mainloop()
