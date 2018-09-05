'''
2. Write a program that produces words-cramble puzzles. The program should choose
words at random from Pride and Prejudice, display the letters of the word in a
random order and challenge the user to guess the original word.

2.1 Start by writing a function called wordlist that takes a filename and compiles a
list of all the unique words found in the file. For example, wordlist('pap.txt')
should return a list of the words in Pride and Prejudice.

In writing this function you will want to add strings to a list only if they are not
already in it. The con dition x not in y holds if x is not one of the items in the
collection called y .
'''

file = open('C:/Users/csguest/Desktop/133-master/Unit 4/pap.txt' ,'r')

import random
