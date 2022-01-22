from tkinter import *
from tkinter import ttk

from time import strftime

root = Tk()
root.title("Clock")


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("Arial", 90), background = "grey", foreground = "orange")
label.pack(anchor='center')


time()

root.mainloop()
