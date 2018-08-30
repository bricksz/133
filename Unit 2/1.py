'''
1. Write a program that counts the number of times the lowercase letter ‘e’ is used in the
file pap.txt .

'''

file = open('C:/Users/csguest/Desktop/133-master/Unit 2/pap.txt', 'r')
string = 'e'
#print(file.read())
counter = 0
for line in file:
    for words in line.split():
        if string in words:
            counter += 1
print(counter)
