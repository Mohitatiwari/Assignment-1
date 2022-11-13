class Account:

    def __init__(self,tittle,Balance):
        self.tittle = tittle
        self.Balance = Balance
         
class SavingsAccount(Account):
        
    def interestRate(self,interestRate):
        return self.tittle,self.Balance,interestRate

a= SavingsAccount("Ashis",5000)
print(a.interestRate(5))

