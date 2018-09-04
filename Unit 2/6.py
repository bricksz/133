'''
6. The builtin
function input displays a string on the screen and returns a string
containing what the user types in response. For example, the statement answer =
input('How are you feeling? ') will display the given question and wait for the user to
type something and press enter. Then answer will be assigned to a string that holds
what the user has typed. Write a program using input that asks the user to type in any
number of words and then reports the maximum number of vowels contained in a
single word, e.g. ‘please’ is a sixletter
word containing three vowels.

'''

def vowel_collector(word):
    emptyset = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    '''
    for x in vowels:
        if x in word:
            emptyset.append(x)   # gives unique vowels only
    '''
    for i in range(len(word)):
        for j in vowels:
            if j == word[i]:
                emptyset.append(j)  # gives total number of vowels , disregarding uniques
    
    return len(emptyset)

def num_vowels():
    text = input('enter as many words and ye shall recieve num of vowels: ')
    textlist = list(map(str, text.split()))   
    current_ix = 0
    current_word = textlist[0]

    
    for word in textlist:
        vol_num = vowel_collector(word)
        if vol_num > current_ix:
            current_ix = vol_num
            current_word = word
        else:
            pass
    print('Highest number of unique vowels in the given word: ', current_word, '\nNumber of unique vowels:', current_ix)
            

num_vowels()
