class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def details(self):
        print(f"The name is {self.name} with id {self.id}")

class Programmer(Employee):
    def showLanguages(self):
        print(f"The default language is Python")

emp1=Programmer("Varun Sharm","2315200034")
emp2=Programmer("Aman Sharm","2315200001")
emp1.details()
emp1.showLanguages()
emp2.details()
emp2.showLanguages()


