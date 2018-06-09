class BankAccount:

    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Cannot open account with debit")
        self.balance = balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount must have a positive value")
        if amount > self.balance:
            raise ValueError("This is not a debit account")
        self.balance = self.balance - amount


    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount must have a positive value")
        self.balance = self.balance + amount


account = BankAccount(500)
print(account.balance)

account.withdraw(250)
print(account.balance)

account.deposit(330)
print(account.balance)

konto = BankAccount(1000)
konto.withdraw(2100)

print(konto.balance)