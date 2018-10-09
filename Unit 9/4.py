'''
Add the enhanced entry widget of Program 9.0.5 to myWidgets.py and use it to
rewrite the wordscramblepuzzle
solver of Program 8.1.
'''

import functions as my
from tkinter import *
from myWidgets import *

def alphabetize(s):
    letters = list(s)
    letters.sort()
    return my.rejoin(letters)

unscramble = {}

with open('pap.txt') as book:
    for line in book:
        for word in my.cleanedup(line).split():
            key = alphabetize(word)
            if key in unscramble:
                if word not in unscramble[key]:
                    unscramble[key].append(word)
            else:
                unscramble[key] = [word]

def solve():
    puzzle = userInput.get()
    key = alphabetize(puzzle)
    if key in unscramble:
        answer = '{0}'.format(unscramble[key])
    else:
        answer = 'No answer found'
    answerLabel['text'] = answer

root = Tk()

userInput = enhancedEntry(root, 'Enter scrambled word:', 'unscramble', solve)
userInput.pack(fill=X)

answerLabel = Label(root)
answerLabel.pack(side=BOTTOM, anchor=W)
