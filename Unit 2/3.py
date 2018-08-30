'''
3. Write a program to determine which word is the shortest of the following: apple,
banana, peach, plum, grapefruit.

'''

fruits = ['apple', 'banana', 'peach', 'plum', 'grapefruit']
counter = len(fruits[0])
current = fruits[0]
for i in fruits:
    num = len(i)
    if num > counter:
        pass
    else:
        counter = len(i)
        current = i
    
print(current)
