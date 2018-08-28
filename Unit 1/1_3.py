'''
1.3. Write a program that checks the word ‘pineapple’ and tells us what vowels it
contains.
'''

vowels = ('a','e','i','o','u')

word = 'pineapple'

emptylist = []
for i in range(len(word)):
    for j in vowels:
        if j == word[i]:
            emptylist.append(j)

print(emptylist)
