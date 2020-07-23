import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Message Box")
root.geometry("640x480")

# Train ticket booking
def info():
    msgbox.showinfo("notice", "Booking Success")


def warn():
    msgbox.showwarning("Warning", "Sold Out")


def error():
    msgbox.showerror("Error", "Payment Error")


def okcancel():
    msgbox.askokcancel("Confirm", "This is for Infant companion.\n Do you want to confirm?")


def retrycancel():
    msgbox.askretrycancel("Retry", "Temporary Error.\n Do you want to retry?")


def yesno():
    msgbox.askyesno("Yes or No", "This is a Reverse Seat.\n Do you want to book?")


def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="This is not saved.\n Do you want to save and close?")
    print("response : ", response)
    if response == 1:
        print("yes")
    elif response == 0:
        print("no")
    else:
        print("cancel")



btn1 = Button(root, command=info, text="Info")
btn2 = Button(root, command=warn, text="Warn")
btn3 = Button(root, command=error, text="Error")

btn4 = Button(root, command=okcancel, text="Confirm")
btn5 = Button(root, command=retrycancel, text="Retry")
btn6 = Button(root, command=yesno, text="Yes or No")
btn7 = Button(root, command=yesnocancel, text="Yes or No or Cancel")

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()
btn7.pack()

root.mainloop()