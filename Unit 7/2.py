'''
2. Use the final version of goalSeek to find all the roots of two from the square root and
the cube root up to the 10 th root. Instead of manually writing different functions to
pass to goalSeek , use a function that creates them for you as they’re needed.
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

def makepower(exp):
    def power(numbers):
        return numbers**exp
    return power

for exp in range(2, 5):
    power = makepower(exp)
    print(goalseek(power, 0, 10, 2, 0.000001))

