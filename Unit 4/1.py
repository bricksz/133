'''
1. Write a program that prints the name Fred 100 times, one time per line.
'''

name = 'Fred'

def zero_to_hund(name, c=100):
    for i in range(c):
        print(i+1, name)

zero_to_hund(name,50)
