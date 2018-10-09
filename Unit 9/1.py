def money(num):
    pattern = '${0:.2f}'
    return pattern.format(num)

class Account:
    def __init__(self, name, amount):
        self.owner = name
        self.balance = amount
        self.transactions = []
        self.runningBalance = amount
    def __str__(self):
        pattern = 'Account of {0}, balance: {1}'
        return pattern.format(self.owner, money(self.balance))
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(['Deposit', amount ])
    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(['Withdrawal', amount])
    def statement(self):
        print(self.transactions)
        pattern = '{0:>12s}{1:>12s}{2:>12s}'
        print(pattern.format('Withdrawls', 'Deposit', 'Balance'))
        print(pattern.format('', '', money(self.runningBalance)))
        for transaction in self.transactions:
            amount = transaction[1]
            if transaction[0] == 'Deposit':
                self.runningBalance += amount
                print(pattern.format('', money(amount), money(self.runningBalance)))
            else:
                self.runningBalance -= amount
                print(pattern.format(money(amount), '', money(self.runningBalance)))
        self.transactions = []

X = Account('John', 300)
X.deposit(5)
X.withdraw(25)
X.statement()