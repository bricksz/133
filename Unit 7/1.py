'''
Use the final version of goalSeek to find the square root of two. Start by defining a
function that squares numbers. Then see what argument value causes this function to
return two.
'''

def goalseek(function, lowlimit, highlimit, target, maxerror=.01):
    error = maxerror + 1
    while error > maxerror:
        guess = (lowlimit+highlimit)/2
        result = function(guess)
        error = abs(result-target)
        if result > target:
            highlimit = guess
        if result < target:
            lowlimit = guess

    return guess

def square(num):
    return num*num

print(goalseek(square, 0, 3, 2))
