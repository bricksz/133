from tkinter import *

translations = {}
word = ''

def translate():
    global word
    word = userinput.get()
    if word in translations:
        answer['text'] = '{} = {}'.format(word )

root = Tk()

topframe = Frame(root)
topframe.pack(fill=X)

prompt = Label(topframe)
prompt['text'] = 'Enter word: '
prompt.pack(side=LEFT)

userinput = Entry(topframe)
userinput.pack(side=LEFT, fill=X)

do = Button(topframe)
do['text'] = 'Translate'
do['command'] = translate
do.pack(side=LEFT)

answer = Label(root)
answer.pack(side=BOTTOM, anchor=W)