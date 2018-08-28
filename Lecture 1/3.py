'''
3. The word ‘substantiate’ contains the word ‘ant’. Write a program that reports which
of the following words is contained in ‘substantiate’: ‘ate’, ‘state’, ‘a’, ‘substantiate’,
‘it’, ‘tan’. The output should look like this:

'''

wordlist = ('ate', 'state', 'a', 'substantiate', 'it', 'tan')
word = 'substantiate'

for x in wordlist:
    if x in word:
        print(x, ' is a substring of ', word)
