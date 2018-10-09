import random

class Card:
    def __init__(self, f, s):
        self.myFaceValue = f
        self.mySuit = s
    def __str__(self):
        return self.myFaceValue +' of ' + self.mySuit
    def faceValue(self):
        return self.myFaceValue
    def suit(self):
        return self.mySuit

class Deck:
    faceValues = ['ace', '2', '3', '4', '5', '6', '7',' 8',
                  '9', '10', 'jack', 'queen', 'king']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']

    def __init__(self):
        self.theCards = [Card(faceValue, suit)
                         for faceValue in Deck.faceValues
                         for suit in Deck.suits]
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.theCards)
    def deal(self):
        return self.theCards.pop()
    def cardsLeft(self):
        return len(self.theCards)


deck1 = Deck()
deck2 = Deck()

'''
while deck1.cardsLeft() > 0:
    card1 = deck1.deal()
    card2 = deck2.deal()
    print('{0:18s}{1:18s}'.format(str(card1), str(card2)),
          end='')
    sameFaceValue = card1.faceValue() == card2.faceValue()
    sameSuit = card1.suit() == card2.suit()
    if sameFaceValue and sameSuit:
        print('Coincidence')
    else:
        print()
'''

class temp:
    somelist1 = ['1', '2', '3']
    somelist2 = ['r', 'g', 'b']
    def __init__(self):