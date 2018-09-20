'''
4. Write a program that solves the wordscramble
puzzles produced by Program 2 in
Unit 4. The user enters a scrambled string of letters and the program responds by
displaying all words in Pride and Prejudice that can be formed by rearranging these
letters.
For this program, you should create a dictionary that has alphabetized strings of
letters as keys and lists of words that can be formed with those letters as the
associated values. For example, the key 'acer' —with the letters in alphabetical
order—would have the value ['care', 'race'] . These four letters can also be rearranged
to form the wor d 'acre' , but this is not used in Pride and Prejudice.
To put a string of letters into alphabetical order, first use it to create a list. Next, use
the list method sort to put the list in order—if your list is called letters , just write
letters.sort() . Finally, use the rejoin function you wrote for Program 2 in Unit 4 to
convert the list back into a string.
'''

import random
import functions as f

emptydict = {}

def ordered(word):
    new = list(word)
    new.sort()
    return f.rejoin(new)

with open('pap.txt') as file:
    for line in file:
        for word in f.cleanedup(line).split():
            key = ordered(word)
            if key in emptydict:
                if word not in emptydict[key]:
                    emptydict[key].append(word)
                else:
                    emptydict[key] = [word]
print(emptydict)
enter = input("Enter: ")
key = ordered(enter)
if key in emptydict:
    print(emptydict[key])
else:
    print("No")
