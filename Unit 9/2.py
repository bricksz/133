'''
Define a new sliding label widget based on the code for Program 9.0.5. Include a
method that sets the text property of the label by sliding it into place from the
lefthand
side. Add this widget to myWidgets.py and use it to rewrite Program 9.0.5.
'''

from tkinter import *
from myWidgets import *


class SlidingLabel(Label):
    def __init__(self, parent):
        Label.__init__(self, parent)
    def slideText(self, text):
        self.word = text
        self['text'] = ''
        self.doSlide()

    def doSlide(self):
        self.charactersToShow = len(result['text']) + 1
        self['text'] = self.word[-self.charactersToShow:]
        if self.charactersToShow < len(self.word):
            root.after(100, self.doSlide)


def go():
    result.slideText(userInput.get())

root = Tk()

quitButton(root)

userInput = enhancedEntry(root, 'Enter text:', 'Go', go)
userInput.pack(fill=X)

result = SlidingLabel(root)
result.pack(side=LEFT, fill=X, anchor=W)
