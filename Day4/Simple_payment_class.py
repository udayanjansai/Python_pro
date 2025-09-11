class Payment:
    def pay(amm):
        pass
class cashpay(Payment):
    def __init__(self,amm):
        self.amm=amm
        
    def pay(self):
        print(f"Paid ₹{self.amm} in cash")
class cardpay(Payment):
    def __init__(self,amm):
        self.amm=amm
        
    def pay(self):
        print(f"Paid ₹{self.amm} using credit/debit card")
class upipay(Payment):
    def __init__(self,amm):
        self.amm=amm
        
    def pay(self):
        print(f"Paid ₹{self.amm} using upi")
payments=[cashpay(1000),cardpay(1000),upipay(1000)]
for p in payments:
    p.pay()


