'''
5. Write a program that repeatedly gets a group of numbers from the user and displays
the average. Define and use a function called average that takes in a list of numbers
and returns the average. Here is a sample run:

> Enter numbers: 1 4 3 2
> Average: 2.5
> Enter numbers: 1 2 3 999
> Average: 251.25
> Enter numbers: 5 2 -7
> Average: 0.0
> Enter numbers:

Note that when you have a string like '12' you can’t use it in an arithmetic expression:
'12'+'34' is '1234' because + means concatenation for strings. The trick is to use the
builtin
function int which converts strings of digit characters into integers: int ( '12') is
12 and int('12')+int('34') is 46 .
'''

def avg():
    ask = input('Enter numbers: ')
    numlist = list(map(int, ask.split()))
    num_ix = len(numlist)
    counter = 0
    for i in numlist:
        counter += i
    return counter/num_ix

if __name__ == '__main__':
    print(avg())
    
