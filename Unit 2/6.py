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

def num_vowels():
    vowels = ['a', 'e', 'i', 'o', 'u']
    text = input('enter as many words and ye shall recieve num of vowels: ')
    textlist = list(map(str, text.split()))

    current = textlist[0]
    emptyset = []
    for word in textlist:
        for x in vowels:
            if x in textlist:
                emptyset.append(x)
    print(len(emptyset))
        
    
    #for word in textlist:
        
    


if __name__ == '__main__':
    num_vowels()
