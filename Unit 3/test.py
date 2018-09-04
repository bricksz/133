emptydict = {}
emptydict['word'] = 1
emptydict['word1'] = 'apple'

while True:
    enter = input('type word: ')
    if enter not in emptydict:
        out = input('attached to word is: ')
        emptydict[enter] = out
    else:
        print('output: ', emptydict[enter])
