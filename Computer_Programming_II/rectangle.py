#Implement a simple class Rectangle that represents a rectangle. 
#The class should have methods to calculate the area and perimeter of the rectangle


class Rectangle:
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width
    def area(self):
        return f"The area of Rectangle is: {self.lenght*self.width}"
    def perimeter(self):
        return f"The perimeter of Rectangle is: {2*(self.lenght+self.width)}"
    
ob1=Rectangle(10,20)
ob2=Rectangle(23,34)
print(ob1.area())
print(ob1.perimeter())
print("\n")
print(ob2.area())
print(ob2.perimeter())