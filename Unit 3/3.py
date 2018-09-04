'''
3. Write a program that compiles information on the number of occurrences of each
word used in Pride and Prejudice. After the information is compiled, the user should
be able to quickly find out how many times any particular words are used.
'''

emptydict = {}
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

switch = True
while switch == True:
    for line in file:
        for word in cleanedup(line).split():
            if word not in emptydict:
                emptydict[word] = 1
            else:
                emptydict[word] += 1
    switch = False

while True:
    input_word = input('Enter word: ')
    if input_word in emptydict:
        print(input_word, '\nNumber of occurances: ', emptydict[input_word])
    else:
        print('None')

