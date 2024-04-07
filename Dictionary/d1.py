# Problem Statement:
# You are given a list of students and their corresponding grades. 
# Create a dictionary where the keys are the student names and the values are their grades. 
# Then, find and print the highest grade without using the max() function.
# Creating the dictionary
grades = {'John': 85, 'Jane': 92, 'Tom': 78, 'Emily': 95, 'Sam': 88}
# Initializing a variable to hold the highest grade
highest_grade = -1
# Iterating through the grades to find the highest
for grade in grades.values():
 if grade > highest_grade:
  highest_grade = grade
# Finding the student(s) with the highest grade
top_students = [student for student, grade in grades.items() if grade == 
highest_grade]
# Printing the highest grade and the student(s)
print(f"The highest grade is: {highest_grade}")
print(f"The student(s) with the highest grade: {','.join(top_students)}")