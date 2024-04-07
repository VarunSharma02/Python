# Problem Statement:
# You are given a list of employees, where each employee is represented as 
# a dictionary with 'name', 'salary', and 'department' keys. 
# Write a program to perform the following tasks:
# Calculate the total salary for each department.
# Find the department with the highest total salary.
# Identify the highest paid employee in each department.
# List of employees
employees = [
 {'name': 'John', 'salary': 50000, 'department': 'Sales'},
 {'name': 'Jane', 'salary': 60000, 'department': 'Sales'},
 {'name': 'Tom', 'salary': 55000, 'department': 'Marketing'},
 {'name': 'Emily', 'salary': 70000, 'department': 'Marketing'},
 {'name': 'Sam', 'salary': 65000, 'department': 'HR'},
 {'name': 'Alex', 'salary': 75000, 'department': 'HR'},
 {'name': 'Sarah', 'salary': 60000, 'department': 'IT'},
 {'name': 'Michael', 'salary': 80000, 'department': 'IT'},
 {'name': 'Jessica', 'salary': 70000, 'department': 'Sales'}
]
# Task 1: Calculate the total salary for each department
department_salaries = {}
for employee in employees:
 department = employee['department']
 salary = employee['salary']
 department_salaries[department] = department_salaries.get(department, 0) + salary

 # Task 2: Find the department with the highest total salary
# highest_salary_department = max(department_salaries, key=department_salaries.get)
highest_salary_department = None
highest_salary = -1
for department, total_salary in department_salaries.items():
 if total_salary > highest_salary:
  highest_salary = total_salary
  highest_salary_department = department
# Printing the department with the highest total salary
print(f"\nDepartment with the highest total salary: {highest_salary_department}")
# Task 3: Identify the highest paid employee in each department
highest_paid_employees = {}
for employee in employees:
 department = employee['department']
 salary = employee['salary']
 if department not in highest_paid_employees or salary > highest_paid_employees[department]['salary']:
  highest_paid_employees[department] = {'name': employee['name'], 'salary': salary}
# Printing results
print("Total salary for each department:")
for department, total_salary in department_salaries.items():
 print(f"{department}: {total_salary}")
print(f"\nDepartment with the highest total salary: {highest_salary_department}")
print("\nHighest paid employee in each department:")
for department, employee_info in highest_paid_employees.items():
 print(f"{department}: {employee_info['name']} (Salary: {employee_info['salary']})")