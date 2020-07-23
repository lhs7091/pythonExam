from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import time

root = Tk()
root.title("Progress Bar")
root.geometry("640x480")
fontstyle = tkFont.Font(size=20)

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) # 1ms단위
# progressbar.pack()
#
# def btncmd():
#     progressbar.stop()
#
#
# btn = Button(root, text="STOP!", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.1) # 0.01 delay

        p_var2.set(i)
        progressbar2.update()
        print(p_var2.get())


btn = Button(root, text="Start!", command=btncmd2)
btn.pack()

progressbar2.pack()


root.mainloop()