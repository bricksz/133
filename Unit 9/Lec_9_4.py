from tkinter import *
from myWidgets import *

class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = 'Quit'
        self['command'] = parent.destroy
        self.pack(side=BOTTOM, anchor=E)

root = Tk()

quitButton(root)

mainloop()

