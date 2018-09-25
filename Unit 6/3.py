'''
Use the shelved versions of Pride and P rejudice and Huckleberry Finn to see which
of the two novels uses longer words on average.
'''

import shelve
import functions as f

def averagewordlength(title):
    shelf = shelve.open('books')
    lines = shelf[title]
    shelf.close()

    number = 0
    totallength = 0

    for line in lines:
        for word in f.cleanedup(line).split():
            number += 1
            totallength += len(word)

    return totallength/number

for title in ['Pride and Prejudice', 'Huckleberry Finn']:
    print(title, averagewordlength(title))
