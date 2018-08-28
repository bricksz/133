'''
1.2. Write a program that produces the following output:

ham on rye
ham on whole wheat
ham on a roll
pastrami on rye
pastrami on whole wheat
pastrami on a roll
roast beef on rye
roast beef on whole wheat
roast beef on a roll
chicken on rye
chicken on whole wheat
chicken on a roll

'''

x = ('rye', 'whole wheat', 'roll')
y = ('ham', 'pastrami', 'roast beef', 'chicken')

for i in y:
    for j in x:
        print(i, "on", j)
