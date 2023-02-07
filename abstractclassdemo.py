from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def payment(self,amt):
        pass
    def gen_slip(self,amt):
        print(amt)
class CrediPayment(Payment):
    def payment(self,amt):
        print("Paid Amount Using Credit card",amt)
    def gen_slip(self,amt): print(amt)
class DebitCard(Payment):
    def payment(self,amt):
        print("Paid amount using Debit card",amt)
    def gen_slip(self,amt):
        print(amt)
obj1=CrediPayment()
obj1.payment(350)
obj1.gen_slip(350)
obj2=DebitCard()
obj2.payment(1200)
obj2.gen_slip(1200)