# Author: Andrew Moore
# A library with the purpose of simplifying the ability to add GUI objects. EX: Buttons
from tkinter import *

class button(object):
    def __init__(self, win, text, command, height=10, width=10):
        self.master = win.master  # Converts graphwin object to tkinter canvas
        self.text = text
        self.command = command
        self.height = height
        self.width = width
        f = Frame(self.master, height=self.height, width=self.width)
        f.pack_propagate(0)  # don't shrink
        f.pack()

        def callback():
            eval(self.command)

        b = Button(f, text=self.text, command=callback)  # Command = Thing to execute on click
        b.pack(fill=BOTH, expand=1)
