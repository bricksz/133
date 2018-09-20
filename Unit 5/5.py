'''
5. Write a program to f ind the five most common words in Pride and Prejudice ending
with ‘ing’. Start by creating a dictionary of counts for all words ending in ‘ing’.
Then use the dictionary to create a list like this:
[[5, 'walking'], [17, 'sing'], [2, 'balancing'], ...]
Each element is a twoitem
list containing a count and a word. Call the list method
sort on this list of lists. The sorting will be done using the first item of the twoitem
lists—that is elements will be sorted from lowest counts at the beginning to highest
counts at the end. The last five elements will then be the ones we want. Use a slice
to select them.
To process all the items in a dictionary, use this pattern:
for key in dictionary:
The name key will be assigned the keys used in dictionary , one at a time, though not
in any predictable order.
'''

import functions as f

emptydict = {}
with open('pap.txt') as file:
    for line in file:
        for word in f.cleanedup(line).split():
            if word in emptydict:
                emptydict[word] += 1
            else:
                emptydict[word] = 1

ingword = []

for word in emptydict:
    if word[-3:] == 'ing':
        ingword.append([emptydict[word],word])

ingword.sort()
print(ingword[:10])
