import random

def rejoin(word_arr):
    text = ''
    for letter in word_arr:
        text += letter
    return text

def scramble(word):
    emptylist = []
    for i in range(len(word)):
        emptylist.append(word[i])
    random.shuffle(emptylist)
    word = rejoin(emptylist)
    return word

word = 'cat'
print(scramble(word))
