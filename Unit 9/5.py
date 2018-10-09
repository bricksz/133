'''
Use the enhanced entry widget of Program 9.0.5 to rewrite the vocabulary learner of
Program 8.2. Be sure that code for the enhanced entry widget is included in
myWidgets.py before you start.
'''

from tkinter import *
from myWidgets import *

word = ''
translations = {}

def translate():
    global word
    word = userInput.get()
    if word in translations:
        answer['text'] = '{0} = {1}'.format(word, translations[word])
    else:
        userInput.setPrompt('Enter translation for {0}'.format(word))
        userInput.setActionText('Save')
        userInput.setAction(save)
        answer['text'] = ''

def save():
    translations[word] = userInput.get()
    userInput.setPrompt('Enter word:')
    userInput.setActionText('Translate')
    userInput.setAction(translate)

root = Tk()

userInput = enhancedEntry(root, 'Enter word:', 'Translate', translate)
userInput.pack(fill=X)

answer = Label(root)
answer.pack(side=BOTTOM, anchor=W)
