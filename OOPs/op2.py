class Employee():
    company="Apple"
    def show(self):
        print(f"THe name of the employee is {self.name} and the company is {self.company}")
    @classmethod
    def changeCompany(cls,newCompany):
        cls.company = newCompany

emp1=Employee()
emp1.name="Varun"
emp1.show()
emp1.changeCompany("Tesla ")
emp1.show()
