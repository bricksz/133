'''
Use the shelved version of the Consumer Price Index data to find the largest
percentage increase in prices ever recorded over the summer months—that is, from
May to September—and the year in which it occurred. Your program should use a
function to compute the percentage increase. If a value increases from begin to end ,
the percentage increase is given by the formula: 100*(end/begin-1)
'''


import shelve

def pctincrease(begin, end):
    return 100*(end/begin-1)

shelf = shelve.open('cpi')
cpi = shelf['cpi']
shelf.close()

maxincrease = 0
for year in range(1913, 2009):
    increase = pctincrease(cpi[year][5],
                           cpi[year][9])
    if increase > maxincrease:
        maxincrease = increase
        maxyear = year

print(maxyear, maxincrease)
