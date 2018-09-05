'''
Write a function called lengths that takes in a list of strings and returns a list of the
lengths of the strings. If we pass it ['Ed', 'Ted', 'Fred', 'Jennifer'] , it will return [2, 3, 4, 8] . Use this function, along with the average function from the previous program
and the cleanedup function, to write a program that accepts sentences from the user
and reports the average length of the words in the sentence.

Other than the function definitions, your program should contain only the following code:

    while True:
        line = input('Enter a sentence: ')
        words = cleanedup(line).split()
        print('Average word length:', average(lengths(words)))
'''

def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

def avg(numlist):
    num_ix = len(numlist)
    counter = 0
    for i in numlist:
        counter += i
    return counter/num_ix

def lengths(words):
    empty = []
    for x in words:
        num = len(x)
        empty.append(num)
    return empty

while True:
    line = input('Enter a sentence: ')
    words = cleanedup(line).split()
    print('Average word length: ', avg(lengths(words)))
