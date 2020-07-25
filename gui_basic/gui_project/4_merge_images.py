from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from PIL import Image
import os

root = Tk()
root.title("Merge Images")


# add file
def add_file():
    files = filedialog.askopenfilenames(title="Select Images",
                                        filetypes=(("PNG file", "*.png"), ("All", "*.*")),
                                        initialdir=r"C:\Users\lhs-DT\Downloads")
    # file information which is selected by user
    for file in files:
        print(file)
        list_file.insert(END, file)


# delete file
def del_file():
    #print(list_file.curselection())
    for index in reversed(list_file.curselection()):
        list_file.delete(index)


# save path(directory)
def browse_dest_path():
    forder_selected = filedialog.askdirectory()
    if forder_selected is None:
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, forder_selected)


def merge_image():
    print(list_file.get(0, END))
    images = [Image.open(x) for x in list_file.get(0, END)]
    # size -> size[0]:width, size[1]:height
    widths = [x.size[0] for x in images]
    heights = [x.size[1] for x in images]

    # get max width and total height
    max_width, total_height = max(widths), sum(heights)

    # layout setting
    result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255))
    y_offset = 0 # distance of each picture
    for idx, img in enumerate(images):
        result_img.paste(img, (0, y_offset))
        y_offset += img.size[1]

        progress = (idx+1) / len(images) * 100
        p_var.set(progress)
        progress_bar.update()

    dest_path = os.path.join(txt_dest_path.get(), "result_image.jpg")
    result_img.save(dest_path)
    msgbox.showinfo("", "Complete")


def start():
    print("width : ", cmb_width.get())
    print("padding : ", cmb_space.get())
    print("format : ", cmb_format.get())

    # file list check
    if list_file.size() == 0:
        msgbox.showwarning("Warn", "There is no File.\nPlease add Files")
        return

    # save path check
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("Warn", "There is save path.\nPlease add save path")
        return

    # image merge
    merge_image()


# file Frame
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=10, text="Add file", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=10, text="Delete", command=del_file)
btn_del_file.pack(side="right")

# list frame
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill='y')

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# save path frame
path_frame = LabelFrame(root, text="save path")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path=Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4, padx=5, pady=5)

btn_dest_path = Button(path_frame, text="Search", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# option frame
frame_option = LabelFrame(root, text="Option")
frame_option.pack(padx=5, pady=5, ipady=5)
# width size option
lbl_width = Label(frame_option, text="width", width=3)
lbl_width.pack(side="left", padx=5, pady=5)

# width size combo box
opt_width = ["Original", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=8)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# padding option label
lbl_space = Label(frame_option, text="padding", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# padding option combo
opt_space = ["No", "Narrow", "wide", "Normal"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=8)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# File format option
lbl_format = Label(frame_option, text="Format", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

# File format combo
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=8)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# Progress bar
frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행 frame
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12, command=start)
btn_start.pack(side="left")

btn_close = Button(frame_run, padx=5, pady=5, text="Close", width=12, command=root.quit)
btn_close.pack(side="right")

root.resizable(False, False)
root.mainloop()
