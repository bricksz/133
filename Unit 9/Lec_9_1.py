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

card1 = Card('jack', 'spades')
card2 = Card('3', 'hearts')

print(card1.faceValue(), card2.suit())
print(card1)