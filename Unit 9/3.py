'''
Define a “reverse” sliding label widget. It works just like the sliding widget in
Program 9.2, but text slides in from the righthand
side of the label. Add the new
widget to myWidgets.py and write a simple GUI program to demonstrate it in action.

It may help you to know that * is defined to mean repetition for strings, so that 5*'ab'
is 'ababababab' .
'''

from tkinter import *
from myWidgets import *

class ReverseSlidingLabel(Label):
    def __init__(self, parent):
        Label.__init__(self, parent)
    def slideText(self, text):
        self.word = text
        self.charactersToShow = 0
        self['text'] = ''
        self.doSlide()
    def doSlide(self):
        self.charactersToShow += 1
        display = ' ' * (len(self.word)-self.charactersToShow)
        display += self.word[:self.charactersToShow]
        self['text'] = display
        if self.charactersToShow < len(self.word):
            root.after(100, self.doSlide)

def go():
    result.slideText(userInput.get())

root = Tk()

quitButton(root)

userInput = enhancedEntry(root, 'Enter text:', 'Go', go)
userInput.pack(fill=X)

result = ReverseSlidingLabel(root)
result.pack(side=LEFT, fill=X, anchor=W)
