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
