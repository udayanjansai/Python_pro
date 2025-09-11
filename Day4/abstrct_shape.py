class Shape:
    def area(self):
        pass

class Circle(Shape):
    

    def area(self,r):
        print("Area of circle:",round( 3.14 * r * r))

class Rect(Shape):
    

    def area(self,l,b):
        print("Area of rectangle:", l * b)



cir = Circle()
cir.area(3)       

rec = Rect()
rec.area(3,4)      
