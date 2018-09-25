'''
6. Write a function f that takes in a number x and returns 17.7/(4x 2 -12x+13) . Then write a
program that asks the user for two floating point numbers, checks the value of f at
100 evenly spaced points between these two numbers and reports the highest value
found. Use the builtin
function max , which takes in a list of values and returns the
highest.
'''

def function(x):
    return 17.7/(4*x**2-12*x+13)

def xvalues(begin, end, num):
    step = (end-begin)/(num-1)
    return [begin+n*step for n in range(num)]

begin = 0
end = 100
print(max([function(x) for x in xvalues(begin, end, 100)]))

'''
for x in xvalues(begin, end, 100):
    print(x)
'''
print(xvalues(-5, 5, 50))

emptylist = []
for p in xvalues(-5,5,50):
    emptylist.append(function(p))

print(max(emptylist))
