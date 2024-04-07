class Math:
    def __init__(self,num):
        self.num = num

    def addtonum(self,n):
        self.num += n

    @staticmethod
    def add(a,b):
         return a+b

a=Math(5)
print(a.num)
a.addtonum(5)
print(a.num)
print(a.add(4,5))

# Instance Varaiable vs class variables

class Employee():
    def __init__(self,name):
        self.name = name
    def showDetails(self):
        print(f"The name of the employee is {self.name}")

emp1=Employee("Varun Sharma")

emp1.showDetails()
# OR
Employee.showDetails(emp1)