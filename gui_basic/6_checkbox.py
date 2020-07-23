from tkinter import *

root = Tk()
root.title("Check box")
root.geometry("640x480")

# chkvar에 int형으로 값을 저장
chkvar = IntVar()
chkbox = Checkbutton(root, text="today close", variable=chkvar)

# default true <-> chkbox.deselect()
chkbox.select()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="A week close", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 1 : check 0: un-check
    print(chkvar2.get())


btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()