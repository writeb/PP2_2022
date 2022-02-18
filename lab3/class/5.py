class Account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self):
        cash = float(input())
        self.balance+=cash
        print("Начислено: ", cash)
    def withdraw(self):
        cash = float(input())
        if self.balance>=cash:
            self.balance-=cash
            print("Снято: ", cash)
        else: 
            b = False
            print("На счету недостаточно средств")
    def __str__(self):
        return f'{self.owner} - {self.balance}'
ac = Account("Name Surname")
ac.deposit()
ac.withdraw()
ac.withdraw()
print(ac)