import functions as f
from tkinter import *
import tkinter

def alphabetize(s):
    letters = list(s)
    letters.sort()
    return f.rejoin(letters)

unscramble = {}

with open('pap.txt') as book:
    for line in book:
        for word in f.cleanedup(line).split():
            key = alphabetize(word)
            if key in unscramble:
                if word not in unscramble[key]:
                    unscramble[key].append(word)
            else:
                unscramble[key] = [word]

def solve():
    puzzle = inputbox.get()
    key = alphabetize(puzzle)
    if key in unscramble:
        answerlabel['text'] = '{0}'.format(unscramble[key])
    else:
        answerlabel['text'] = 'No answer found'

root = Tk()

inputframe = Frame(root)
inputframe.pack(fill=X)

inputbox = Entry(inputframe)
inputbox.pack(side=LEFT, fill=X)

inputboxlabel = Label(inputframe)
inputboxlabel['text'] = 'Enter scrambled word: '
inputboxlabel.pack(side=LEFT, fill=X)

button = Button(inputframe)
button['text'] = 'unscramble'
button['command'] = solve
button.pack(side=LEFT, fill=X)

answerlabel = Label(root)
answerlabel.pack(side=BOTTOM, anchor=W)

mainloop()