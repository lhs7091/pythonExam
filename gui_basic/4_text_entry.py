from tkinter import *

root = Tk()
root.title("Text Entry")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)
e.pack()

e.insert(0, "input one line")


def btncmd():
    # print Contents
    # 1.0, END => from line 1 and 0 column to End
    print(txt.get("1.0", END))
    print(e.get())

    # delete contents
    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()