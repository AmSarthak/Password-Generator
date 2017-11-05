import tkinter
from tkinter import *
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
import random
import sys
import os

chars="abcdefghijklmnopqrstuvwxyz1234567890.;_@$"

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def password_generate():
    x=int(e1.get())
    y=int(e2.get())
    for a in range(x):
        password=''
        for i in range(y):
            password+=random.choice(chars)
        msg = Message(master, text = password)
        msg.config(bg='lightblue', font=('times', 18, 'normal'))
        msg.grid(row=6)

master = Tk()
master.title("Password Generator")
Label(master, text="Enter number of passwords:").grid(row=0)
Label(master, text="Enter number of digits:").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Submit' , command=password_generate).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Reset' , command=restart_program).grid(row=4, column=1, sticky=W, pady=4)

mainloop()
