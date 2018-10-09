from tkinter import *

class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = 'Quit'
        self['command'] = parent.destroy
        self.pack(side=BOTTOM, anchor=E)

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

class multipleEntry(Frame):
    def __init__(self, parent, promptText, actionText, action):
        Frame.__init__(self, parent)
        self.prompt = Label(self)
        self.prompt['text'] = promptText
        self.prompt.pack(anchor=W)

        self.entries = [self.makeEntryFrame()]
        self.moreButton = self.makeMoreButton()

        self.actionButton = Button(self)
        self.actionButton['text'] = actionText
        self.actionButton['command'] = action
        self.actionButton.pack(side=BOTTOM, anchor=W)

    def makeEntryFrame(self):
        self.lastFrame = Frame(self)
        self.lastFrame.pack(fill=X, anchor=W)
        entry = Entry(self.lastFrame)
        entry.pack(side=LEFT)
        return entry

    def makeMoreButton(self):
        button = Button(self.lastFrame)
        button['text'] = 'More'
        button['command'] = self.addEntry
        button.pack(side=LEFT)
        return button

    def addEntry(self):
        self.entries.append(self.makeEntryFrame())
        self.moreButton.destory()
        self.moreButton = self.makeMoreButton()

    def get(self):
        return [entry.get() for entry in self.entries]
