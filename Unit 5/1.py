'''
1. Write a program that prints the name Fred 100 times, one time per line. Do not use
for or while . Instead, create a function called printFred that takes in a number and
prints Fred that number of times. The function operates by displaying the name Fred
once and then calling itself with the next smaller number, if that number is at least
one. The call printFred(100) should do what we want.
A function that calls itself is said to be recursive . As this program demonstrates,
recursion can always be used in place of loops.
'''

def print_fred(n):
    if n > 0:
        print_fred(n - 1)
        print('Fred')

print_fred(5)
