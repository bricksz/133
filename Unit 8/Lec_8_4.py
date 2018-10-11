from tkinter import *
import random

numbershares=0
account=10000
shareprice=97

def update():
    shares['text'] = 'You own {0} shares'.format(numbershares)
    cash['text'] = 'Cash balance: ${0:.0f}'.format(account)
    totalworth = account + numbershares*shareprice
    worth['text'] = 'Total worth: ${0:.0f}'.format(totalworth)
    price['text'] = '${0:.2f}/share'.format(shareprice)

def dobuy():
    global account, numbershares
    if account >= 10*shareprice:
        numbershares += 10
        account -= 10*shareprice
        update()
        
def dosell():
    global account, numbershares
    if numbershares >= 10:
        numbershares -= 10
        account += 10*shareprice
        update()

def changeprice():
    global shareprice
    shareprice += random.random()*4 - 2
    update()
    root.after(500, changeprice)


root = Tk()
root['bg'] = 'light yellow'

status = Frame(root)
status['bg'] = 'light green'


shares = Label(status)
shares['text'] = 'Number of Shares'
shares.pack(anchor=W)

cash = Label(status)
cash['text'] = 'Cash on hand'
cash.pack(anchor=W)

worth = Label(status)
worth['text'] = 'Total worth'
worth.pack(side=BOTTOM, anchor=W)

action = Frame(root)
action['bg'] = 'pink'

price = Label(action)
price['text'] = 'Price of stock'
price.pack(anchor=E)

sell = Button(action)
sell['text'] = 'sell'
sell['command'] = dosell
sell.pack(side=BOTTOM, fill=X)

buy = Button(action)
buy['text'] = 'buy'
buy['command'] = dobuy
buy.pack(side=BOTTOM, fill=X)

status.pack(side=LEFT, expand=YES, fill=BOTH)
action.pack(side=RIGHT, expand=YES, fill=BOTH)

changeprice()

mainloop()
