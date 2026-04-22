class Maths:
    def area(self):
        pass

class Circle(Maths):
    def __init__(self,radius):
        self.radius=radius
        print("area",3.14*radius*radius) 
        
            

c=Circle(20)  

class Rect(Maths):
     def __init__(self,le,br):
         self.le=le
         self.br=br
         print("area is ",le*br)

d=Rect(5,4)        

class Square(Maths):
    def __init__(self,a):
        self.a=a
        print("area is ",a*a)

e=Square(3)               
     
class Tri(Maths):
    def __init__(self,b,h):
        self.b=b
        self.h=h
        print("area is ",1/2*b*h)      

f=Tri(4,6)   

    

