'''
1. Reuse the cleanedup function in a program that finds the longest word used in Pride
and Prejudice. Note that if you use split without cleanedup , your program will find
‘inconveniencescheerfulness’, which is long, but not a single word.
'''
file = open('C:/Users/csguest/Desktop/133-master/133-master/Unit 2/pap.txt', 'r')

def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext
    

current = []
current_ix = 0
for line in file:
    t_line = cleanedup(line)
    for word in t_line.split():
        if len(word) > current_ix:
            current_ix = len(word)
            current = word
        else:
            pass
print('Word: ', current, '\nLength: ', current_ix) 

