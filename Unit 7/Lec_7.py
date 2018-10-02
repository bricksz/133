
def pctIncrease(begin, end):
    return 100*(end/begin-1)
def increaseByPct(begin, pct):
    return begin+begin*pct/100
def totalPct(pct):
    startValue = 175.1
    value = startValue
    for year in range(5):
        value = increaseByPct(value, pct)

    return pctIncrease(startValue, value)

def totalPct2(pct):
    startValue = 154.4
    value = startValue
    for year in range(10):
        value = increaseByPct(value, pct)
    return pctIncrease(startValue, value)


def goalSeek(function,lowLimit, highLimit, target, maxerror=.01):
    error = maxerror + 1
    
    while error > maxerror:
        guess = (lowLimit+highLimit)/2
        result = function(guess)
        error = abs(result-target)
        if result > target:
            highLimit = guess
        if result < target:
            lowLimit = guess
            
    return guess
print(goalSeek(totalPct,-100, 100, 13.2))

print(goalSeek(totalPct2, -100, 100, 13.2,.000001))

