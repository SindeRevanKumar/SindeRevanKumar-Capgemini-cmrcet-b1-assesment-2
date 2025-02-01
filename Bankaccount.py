# 2. Design a `BankAccount` class with `deposit()` and `withdraw()` methods.
#  Implement logic to prevent overdraft.
from abc import ABC,abstractmethod
class Bankaccount:
     
    @abstractmethod
    def deposit(self,amount):
        pass
    def withdraw(self,amount):
        pass


class Account(Bankaccount):
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self, amount):
        self.amount=amount
        self.balance+=self.amount
        print(f"The amount {self.amount} has been added to your account")
    def withdraw(self,amount):
        self.amount=amount
        self.balance-=self.amount
        print(f"The amount {self.amount} has been deducted from your account")
    def check_balance(self):
        print(f"The available balance is : {self.balance}")

acc=Account()
n=1
while n!=0:
    choose=int(input("1.Deposit\n2.withdraw\n3.check_balance\n0.exit :"))
    if choose==1:
        depo=int(input("Enter the amount you want to deposit : "))
        acc.deposit(depo)
    elif choose==2:
        withdr=int(input('enter the amount you want to withdraw : '))
        acc.withdraw(withdr)
    elif choose==3:
        acc.check_balance()
    else:
        print("Thankyou for using our bank account......:)")
        n=0

