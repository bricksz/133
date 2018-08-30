'''
4. Write a program to determine the average of the numbers given in a list. The first
line of your program should give a name to a list of numbers to be averaged: e.g.
numbers = [3, 17, 1, 44, 239].

'''

def avg_num():
    counter = 0
    num = input('enter yo numbers: ')
    numlist = list(map(int, num.split()))
    lenlist = len(numlist)
    for i in numlist:
        counter += i
        avg = counter / lenlist
    return avg

print(avg_num())
