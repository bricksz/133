def goalseek(function, limit1, limit2,
             target, maxerror = .01):
    result1 = function(limit1)
    result2 = function(limit2)

    if result1 < target < result2:
        return goalseeker(function, limit1, limit2,
                          target, maxerror)

    if result2 < target < result1:
        return goalseeker(function, limit2, limit1,
                          target, maxerror)

    return None

def goalseeker(function, lowlimit, highlimit,
             target, maxerror=.01):
    error = maxerror + 1

    while error > maxerror:
        guess = (lowlimit + highlimit)/2
        #print('lo={0} hi={1}'.format(lowlimit, highlimit))
        result = function(guess)
        #print('guess={0} result{1}'.format(guess, result))
        error = abs(result - target)
        #print('error={0}'.format(error))
        if result > target:
            highlimit = guess
        if result < target:
            lowlimit = guess
        #print('lo={0} hi={1}'.format(lowlimit, highlimit))

    return guess

def mystery(x):
    return x*x - 10*x + 25

print(goalseek(mystery, 0, 5, 10, .001))
print()

#print(goalseek(mystery, 10, 20, 10, .001))