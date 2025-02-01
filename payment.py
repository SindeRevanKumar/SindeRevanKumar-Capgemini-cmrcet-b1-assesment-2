# Write a `Payment` class with a method `process_payment()`.
#  Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` that override the 
# method differently.
from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def Process_payment(self,amount):
        pass
class CreditCardPayment(Payment):
    def Process_payment(self, amount):
        self.amount=amount
        print(f"the {amount} is debited from CreditCardPayment")
class PayPalPayment(Payment):
    def Process_payment(self, amount):
        self.amount=amount
        print(f"the {amount} is debited from PayPalPayment")
class BitcoinPayment(Payment):
    def Process_payment(self, amount):
        self.amount=amount
        print(f"the {amount} is debited from BitcoinPayment")    

c=CreditCardPayment()
c.Process_payment(10)
P=PayPalPayment()
P.Process_payment(10)
b=BitcoinPayment()
b.Process_payment(10)