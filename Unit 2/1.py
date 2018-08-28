'''
1. Write a program that counts the number of times the lowercase letter ‘e’ is used in the
file pap.txt .

'''

file = open('C:/Users/csguest/Desktop/Unit 2/pap.txt', 'r')
#print(file.read())

for line in file:
    if 'property' in line:
        print(line)
