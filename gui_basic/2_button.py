from tkinter import *
import random

root = Tk()

root.title("GUI Start")

#Add Button
btn1 = Button(root, text="button 1")
btn1.pack()

# padx, pady = padding
btn2 = Button(root, padx=5, pady=10, text="button 22222222")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="button 3")
btn3.pack()

# width, height = fix size
btn4 = Button(root, width=10, height=3, text="button4444444")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="button5")
btn5.pack()

photo = PhotoImage(file="./pics/arrow-30330_1280.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("click btn")
    print(random.randint(1,30))


btn7 = Button(root, text="command button", command=btncmd)
btn7.pack()

root.mainloop()