'''
2. Write a program that learns vocabulary in a language other than English. It asks the
user for words in English, gives the translation if it has seen the word before and, if
not, asks the user to enter it. Here is a sample run.

    Enter English word: cat
    Enter translation: gato
    Enter English word: dog
    Enter translation: perro
    Enter English word: cat
    cat = gato
    Enter English word: cow
    Enter translation: vaca
    Enter English word: dog
    dog = perro
    Enter English word:
'''

emptydict = {}
while True:
    eng_word = input('Enter English word: ')
    if eng_word not in emptydict:
        tran_word = input('Enter translation: ')
        emptydict[eng_word] = tran_word
    else:
        print(eng_word, '=', emptydict[eng_word])
    
