import random

class Card:
    def __init__(self, f, s):
        self.myFaceValue = f
        self.mySuit = s
    def __str__(self):
        return self.myFaceValue+ ' of '+ self.mySuit
    def faceValue(self):
        return self.myFaceValue
    def suit(self):
        return self.mySuit

class Deck:
    faceValues = ['ace', '2','3','4','5','6','7','8','9','10',
                  'jack','queen','king']
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

class personalDeck(Deck):
    def __init__(self, name):
        Deck.__init__(self)                         # Carrying out all of the init of Deck
        self.owner = name
    def __str__(self):
        return "{0}'s deck".format(self.owner)

pd = personalDeck('John')
print(pd)
print(pd.cardsLeft())