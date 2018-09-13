'''
4. Write a program that randomly chooses a hand of five cards from a standard deck of
playing cards and displays it for the user to see. Use a function that returns a shuffled
deck, ready for dealing.

A standard deck consists of 52 cards. There are 13 each of four suits : clubs,
diamonds, hearts and spades. Within each suit, the 13 face values are: ace, 2, 3, 4, 5,
6, 7, 8, 9, 10, jack, queen and king. We identify a card by its face value and suit, e.g.
the 2 of hearts, the jack of clubs, etc.
'''

import random as r
import functions as f

def deal():
    face_card = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King', 'Ace']
    suit = ['Spade','Heart','Clover','Diamond']

    deck = []
    for i in suit:
        for j in face_card:
            card = [j, '_', i]
            card = f.rejoin(card)
            deck.append(card)

    hand = []
    for k in range(5):
        select_card = r.choice(deck)
        deck.remove(select_card)
        hand.append(select_card)

    print(hand)
    return hand
