'''
6. Write a program that tells us which vowels are used in each of the following words:
‘apple’, ‘banana’, ‘peach’, ‘grapefruit’. The output should look like this:

Vowels in apple
a
e
Vowels in banana
a
Vowels in peach
a
e
Vowels in grapefruit
a
e
i
u
2
'''

wordlist = ('apple', 'banana', 'peach', 'grapefruit')
vowels = ('a','e','i','o','u')

for x in wordlist:
    emptylist = []
    for i in range(len(x)):
        for j in vowels:
            if j == x[i]:
                if j not in emptylist:
                   emptylist.append(j)
    print("Vowels in",x)
    for k in emptylist:
        print(k)
    
