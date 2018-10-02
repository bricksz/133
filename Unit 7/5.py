'''
Write a program to produce an alphabetized phone directory based on data in a file.
The data file uses the following ‘tabdelimited’
format—there is a tab character
between the family and given names and between the given name and the phone
number.
Smith John 212-745-1234
Mayflower Abigail Lou 718-255-6656
Brown-Appleby Anthony 516-778-9813
The output should use the following format:
Brown-Appleby, Anthony (516) 778-9813
Mayflower, Abigail Lou (718) 255-6656
Smith, John (212) 745-1234
It will help you to know that the string method split includes an optional argument
that specifies the string to be considered as a separator. For example,
'abcdbcda'.split('b') returns ['a', 'cd', 'cda'] .

'''

entries = []

with open('phoneData.txt') as data:
    for line in data:
        items = line.split('\t')
        name = items[0] + ', '+item[1]
        area = items[2][:3]
        number = item[2][4:-1]
        entries.append([name,area, number])

entries.sort()

for entry in entries:
    print('{0:24s}({1}) {2}'.format(entry[0],entry[1],entry[2]))
