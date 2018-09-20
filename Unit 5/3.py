'''
3. Write a program that reports the total number of files in the current directory and any
subdirectories, subsubdirectories and so on.
'''

import os
path = '.'

def lister(path):
    counter = 0
    for filename in os.listdir(path):
        newpath = os.path.join(path, filename)
        if os.path.isdir(newpath):
            counter += lister(newpath)
            counter +=1
        else:
            counter += 1
    return counter
Parentofparent = os.path.join('..','..')
# '..\..'
print(lister('..\..'))
