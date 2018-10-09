import random

def rejoin(word_arr):
    text = ''
    for letter in word_arr:
        text += letter
    return text

def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total/len(numbers)

def scramble(word):
    emptylist = []
    for i in range(len(word)):
        emptylist.append(word[i])
    random.shuffle(emptylist)
    word = rejoin(emptylist)
    return word

def word_arr():
    file = open('C:/Users/csguest/Desktop/133-master/Unit 4/pap.txt' ,'r')
    emptylist = []

    for line in file:
        for word in cleanedup(line).split():
            if word not in emptylist:
                emptylist.append(word)
            else:
                pass
    return emptylist

def deal():
    face_card = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King', 'Ace']
    suit = ['Spade','Heart','Clover','Diamond']

    deck = []
    for i in suit:
        for j in face_card:
            card = [j, '_', i]
            card = rejoin(card)
            deck.append(card)

    hand = []
    for k in range(5):
        select_card = random.choice(deck)
        deck.remove(select_card)
        hand.append(select_card)

    return hand

def count_card(hand,face,suit):
    face_ix = 0
    suit_ix = 0
    for x in hand:
        if face in x:
            face_ix += 1
        if suit in x:
            suit_ix += 1
    return hand, face_ix, suit_ix