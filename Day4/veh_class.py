class veh:
    def __init__(self,li,name,spot):
        self.__li=li
        self.__name=name
        self.__spot=spot
    def display():
        pass
class bike(veh):
    def __init__(self,li,name,spot,hel):
        super().__init__(li,name,spot)
        self.__hel=hel
    def display(self):
        print("name: ",self.name,"\n")
        print("li: ",self.li,"\n")
        print("spot: ",self.spot,"\n")
        print("helmet available: ",self.hel)

class car(veh):
    def __init__(self,li,name,spot,seats):
        super().__init__(li,name,spot)
        self.__seats=seats
    def display(self):
        print("name: ",self.name,"\n")
        print("li: ",self.li,"\n")
        print("spot: ",self.spot,"\n")
        print("helmet available: ",self.hel)

class suv(veh):
    def __init__(self,li,name,spot,fo):
        super().__init__(li,name,spot)
        self.__fo=fo
    def display(self):
            print("name: ",self.name,"\n")
            print("li: ",self.li,"\n")
            print("spot: ",self.spot,"\n")
            print("four wheel drive: ",self.fo)

class truuck(veh):
    def __init__(self,li,name,spot,load):
        super().__init__(li,name,spot)
        self.__load=load
    def display(self):
            print("name: ",self.name,"\n")
            print("li: ",self.li,"\n")
            print("spot: ",self.spot,"\n")
            print("load: ",self.load)

