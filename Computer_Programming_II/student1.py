#Create a class Student with attributes name, age, and grade. 
#Implement a method to display the student details. 
#Create instances of the Student class and display their details
class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def details(self):
        return f"The Student Detaits is:\n Name:{self.name}\n Age:{self.age}\n Grade:{self.grade}"
# User input method
name=input("Enter the Student's name:")
age=input("Enter the Student's age:")
grade=input("Enter the Student's grade:")
std1 = Student(name, age, grade)
print(std1.details())

#Instance method
std1=Student("Aman",20,"A")
std2=Student("Varun",19,"c")
std3=Student("Pratham",20,"B") 
print(std1.details())
print(std2.details())
print(std3.details())
