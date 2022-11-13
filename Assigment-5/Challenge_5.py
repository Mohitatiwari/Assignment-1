class Account:

    def __init__(self,balance):
        self.balance = balance
    
    def getBalance(self):
        print(self.balance)

    def deposit(self,ammount):
        self.balance=ammount+self.balance

    def withdrawal(self,withdrawal):
        self.balance=self.balance-withdrawal

class SavingsAccount(Account):
        
    def interestAmmount(self,interestRate):
        return (interestRate*self.Balance)/100

a= Account(2000)
a.deposit(200)
a.getBalance()
b = SavingsAccount
print(b.interestAmmount(1))


