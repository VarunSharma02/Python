print("Employee Database Menu:")
print("1. Add new employee")
print("2. Retrieve employee information")
print("3. Update employee salary")
print("4. Display all employees")
print("5. Exit")
data={}
choice=int(input(("Enter your choice (1-5):")))

id=int(input("Enter Employee ID:"))
name=input("Enter the name of the employee:")
age=int(input("Enter the age of the employee"))
gender=(input("Enter the gender of the employee"))
position=(input("Enter the position of the employee"))
salary=int(input("Enter the salary of the employee"))

data["Name:"]=name
data["Age"]=age
data["Gender:"]=gender
data["Position:"]=position
data["Salary"]=salary

print(data)
if choice == 1:
 print(f"Employee Information for ID{id}:")
 print(f"Name:{name}")
 print(f"Age:{age}")
 print(f"Gender:{gender}")
 print(f"Position:{position}")
 print(f"Salary:{salary}")

elif choice == 2:
 id=int(input("Enter the employee ID to retrieve the information:"))
 if id in data[id]:
  print(f"Employee Information for ID{id}:")
  print(f"Name:"{name}"])
  print(f"Age:{age}")
  print(f"Gender:{gender}")
  print(f"Position:{position}")
  print(f"Salary:{salary}")
 else:
  print("Given ID is not Valid!")
elif choice ==3:
 update=int(input("Enter the  employee ID to update the salary:"))
 new=int(input("Enter the new salary:"))
data["salary"]=new
 print("Salary has been updated")
elif choice ==4:
 print("All Employees:")
 print(data)
 print(f"Employee Information for ID{id}:")
 print(f"Name:{name}")
 print(f"Age:{age}")
 print(f"Gender:{gender}")
 print(f"Position:{position}")
 print(f"Salary:{salary}")
else:
  print("Exiting the program")