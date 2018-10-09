from tkinter import *
from myWidgets import *

'''
class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = 'Quit'
        self['command'] = parent.destroy
        self.pack(side=BOTTOM, anchor=E)

root = Tk()

quitButton(root)

mainloop()


class enhancedEntry(Frame):
    def __init__(self, parent, prompt, actionText, action):
        Frame.__init__(self, parent)

        self.inputBoxLabel = Label(self)
        self.inputBoxLabel['text'] = prompt
        self.inputBoxLabel.pack(side=LEFT, fill=X)

        self.inputBox = Entry(self)
        self.inputBox.pack(side=LEFT, fill=X)

        self.button = Button(self)
        self.button['text'] = actionText
        self.button['command'] = action
        self.button.pack(side=LEFT, fill=X)

    def get(self):
        return self.inputBox.get()

    def setActionText(self, actionText):
        self.button['text'] = actionText

    def setPrompt(self, prompt):
        self.inputBoxLabel['text'] = prompt

    def setAction(self, cmd):
        self.button['command'] = cmd
'''

word = ''

def slide():
    global word
    word = userInput.get()
    result['text'] = ''
    doSlide()

def doSlide():
    charactersToShow = len(result['text']) + 1
    result['text'] = word[-charactersToShow:]
    if charactersToShow < len(word):
        root.after(100, doSlide)

root = Tk()

quitButton(root)

userInput = enhancedEntry(root, 'Enter text:', 'Go', slide)
userInput.pack(fill=X)

result = Label(root)
result.pack(side=LEFT, fill=X, anchor=W)

mainloop()
