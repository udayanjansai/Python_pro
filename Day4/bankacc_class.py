class bank:
    def __init__(self,balance=0):
        self.__bal=balance
    def depo(self,d):
        self.__bal+=d
    def withd(self,w):
        if w<=self.__bal:
            self.__bal-=w
        else:
            print("Insufficient funds\n")
    def get(self):
        print("bank balance: ",self.__bal)
p=bank(1000)
p.depo(5000)
p.withd(2000)
p.get()
        