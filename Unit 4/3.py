'''
3. Most of the puzzles produced by the previous program are much too hard. Modify
the program so that it gives the user a threeletter
puzzle to start and then adjusts the
number of letters up by one every time a correct answer is given and down by one for
every wrong answer. In this way, the program will generally produce puzzles that are
at the user’s level.

Rather than keeping all possible words in a single list, you should use a dictionary. If
the dictionary is called wordlists , then wordlists[7] should be a list of all words in
Pride and Prejudice that are seven letters long.
'''
import random
import functions as f


def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext
    

def max_word(list_words):
    current = []
    current_ix = 0
    for word in list_words:
        if len(word) > current_ix:
            current_ix = len(word)
            current = word
        else:
            pass
    return current

def unscramble_setup(words_in_array):
    selected_word = random.choice(words_in_array)
    scrambled_word = f.scramble(selected_word)

    print("The word is: ", scrambled_word)
    user_input = input("Please unscramble the word: ")
    if user_input == selected_word:
        print("You win")
    else:
        print("Try again")
        


wordlists = {}
list_words = f.word_arr()
max_ix = len(max_word(list_words))
for i in range(max_ix):
    wordlists.setdefault(i, [])
    for j in list_words:
        if i == len(j):
            wordlists[i].append(j)
            

counter = 3
while counter < 18:
    select_word = random.choice(wordlists[counter])
    scrambled_word = f.scramble(select_word)
    print("The word is: ", scrambled_word)
    user_input = input("Please unscramble the word: ")
    if user_input == select_word:
        print("You win")
        counter += 1
    else:
        print("Try again")
