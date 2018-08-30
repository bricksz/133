'''
5. The list method append changes a list by adding an item at the end. For example if
students refers to the list ['Ed' 'Ted', 'Fred'] , then after calling
students.append('Jennifer') the list will be ['Ed' 'Ted', 'Fred', 'Jennifer'] . Write a
program using this method to print a list of the lengths of the words given in a list.
The first line of your program should give a name to the list of words, e.g. students =
['Ed', 'Ted', 'Fred', 'Jennifer'] . For this example, the output would be [2, 3, 4, 8] .

'''
def len_names():
    names = input('enter yo names: ')
    namelist = list(map(str, names.split()))
    emptylist = []
    for name in namelist:
        namelen = len(name)
        emptylist.append(namelen)
    print(emptylist)

if __name__ == '__main__':
    len_names()
