'''
Write a progra m to add Pride and Prejudice to the shelve object that holds
Huckleberry Finn.
'''

import shelve

with open('pap.txt') as book:
    lines = book.readlines()

shelf = shelve.open('books')
newlines = shelf['Pride and Prejudice']
print(newlines[100])
self.close()
