import random
import cards
from tkinter import *

faceValues = ['ace', '2', '3', '4', '5', '6',
'7', '8', '9', '10', 'jack',
'queen', 'king']
suits = ['clubs', 'diamonds', 'hearts',
'spades']
def shuffledDeck():
    deck = []
    for faceValue in faceValues:
        for suit in suits:
            deck.append(faceValue + ' of ' + suit)
    random.shuffle(deck)
    return deck

def firstCard():
    deck = cards.shuffledDeck()
    card['text'] = deck[0]

root = Tk()

card = Label(root)
card.pack

pick = Button(root)
pick['text'] = 'Pick a card'
pick['command'] = firstCard
pick.pack()

mainloop()
