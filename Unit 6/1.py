'''
Write and test a function called lengths that takes in a list of strings and returns a list
of the lengths of the strings. If we pass it ['Ed', 'Ted', 'Fred', 'Jennifer'] , it will return
[2, 3, 4, 8] . Your function should use a list comprehension.
'''

def lengths(array):
    return [len(s) for s in array]

names = ['Ed', 'Ted', 'Fred', 'Jennifer']
print(lengths(names))
