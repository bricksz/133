'''
A bank is open from 9 a.m. to 5 p.m. There is one teller. Customers arrive at random times, averaging 20 per hour.

Each needs a random amount of time with the teller, ranging from one to five minutes.

When one customer is with the teller, others wait on a line.

Write a simulation program to find out, on average, how long the line at the bank will be.

Then rerun the simulation with an average of 25 customers arriving per hour.

You may find the following function useful. It returns True with probability p :

def chance(p):
    return random.random()<p

Suppose, for example, that we pass in .3. The random.random function picks a
number at random between 0 and 1.

There is a 30 percent chance that this number
will happen to be lower than .3, so there is a 30 percent chance that the chance function will return True .

We use the function this way:
if chance(.3):

In this case, there is a 30 percent chance that the ‘something’ in the body of the if
statement will happen.
'''


import random

def chance(p):
    return random.random() < p

secondsPerMinute = 60
secondsPerHour = 60*secondsPerMinute
secondsPerWorkDay = 8*secondsPerHour

arrivalProbability = 20/secondsPerHour

class Customer:
    def __init__(self):
        self.transactionTime = (1 + random.random()*4) * secondsPerMinute


class Bank:
    def __init__(self):
        self.time = 0
        self.line = []
        self.servingCustomer = False
    def lineLength(self):
        if len(self.line) < 2:
            return 0
        else:
            return len(self.line) - 1
    def doOneSecond(self):
        self.time += 1
        if chance(arrivalProbability):
            self.line.append(Customer())
        self.finishCustomer()
        self.startCustomer()
    def finishCustomer(self):
        if self.servingCustomer and self.time == self.line[0].endTime:
            self.line = self.line[1:]
            self.servingCustomer = False
    def startCustomer(self):
        if self.servingCustomer:
            return False
        elif len(self.line) > 0:
            self.servingCustomer = True
            self.line[0].endTime = self.time + self.line[0].transactionTime

pattern = 'Average line length: {0:4.1f}'
for simulation in range(10):
    theBank = Bank()
    total = 0
    while theBank.time < secondsPerWorkDay:
        theBank.doOneSecond()
        total += theBank.lineLength()
    print(pattern.format(total/secondsPerWorkDay))
