'''
2. Write a program that produces words-cramble puzzles. The program should choose
words at random from Pride and Prejudice, display the letters of the word in a
random order and challenge the user to guess the original word.

2.1 Start by writing a function called wordlist that takes a filename and compiles a
list of all the unique words found in the file. For example, wordlist('pap.txt')
should return a list of the words in Pride and Prejudice.

In writing this function you will want to add strings to a list only if they are not
already in it. The con dition x not in y holds if x is not one of the items in the
collection called y .

2.2 In order to scramble a string, you’ll have to start by turning it into a list of
individual characters. After the list is rearranged randomly, you’ll want to put the
characters back together into a single string. Write a function called rejoin that
does this. The call rejoin(['c', 'a', 't']) should return the string 'cat' .

2.3 Write a function called scramble that takes in a string and returns a string with the
same letters in a random order.
Finally, use these three functions to write the puzzle program.
'''
import random
import functions as f


def word_arr():
    file = open('C:/Users/csguest/Desktop/133-master/Unit 4/pap.txt' ,'r')
    emptylist = []

    for line in file:
        for word in f.cleanedup(line).split():
            if word not in emptylist:
                emptylist.append(word)
            else:
                pass
    return emptylist

def unscramble_setup(words_in_array):
    
    selected_word = random.choice(words_in_array)
    scrambled_word = f.scramble(selected_word)

    print("The word is: ", scrambled_word)
    user_input = input("Please unscramble the word: ")
    if user_input != selected_word:
        print("Try again")
    else:
        print("You win")

if __name__ == '__main__':
    words_in_array = word_arr()
    while True:
        unscramble_setup(words_in_array)       
            
