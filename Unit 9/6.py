from tkinter import *
from myWidgets import *

def pick():
    names = userInput.get()
    favorite['text'] = 'My favorite name is '
    for name in names:
        if len(name) >= 5:
            favorite['text'] += name
            return
    favorite['text'] += names[0]

root = Tk()

userInput = multipleEntry(root, 'Enter name: ', 'Pick favorite', pick)
userInput.pack(expand=YES, fill=BOTH)

favorite = Label(root)
favorite.pack(side=BOTTOM, anchor=W)

    
