word = 'banana'
vowels = ('a','e','i','o','u')

emptylist = []

for i in range(len(word)):
    for j in vowels:
        if j == word[i]:
            emptylist.append(j)
print("Vowels in", word)
for k in emptylist:
    print(k)
