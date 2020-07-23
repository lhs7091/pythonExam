from tkinter import *

root = Tk()
root.title("GUI Label")
root.geometry("640x480")

label1 = Label(root, text="Hello")
label1.pack()

photo = PhotoImage(file="./pics/arrow-30330_1280.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    global photo2
    label1.config(text="GoodBye")
    photo2 = PhotoImage(file="./pics/arrow-304924_1280.png")
    label2.config(image=photo2)


btn = Button(root, text="Click", command=change)
btn.pack()


root.mainloop()