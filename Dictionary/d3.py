# Problem Statement:
# You have a list of students with their corresponding grades and a list of subjects. 
# Write a program to create a report card for each student, 
# with grades for each subject and the overall average.
students = ['John', 'Jane', 'Tom', 'Emily', 'Sam']

grades = {'John': {'Math': 85, 'Science': 90, 'History': 75}, 
 'Jane': {'Math': 92, 'Science': 88, 'History': 85},
 'Tom': {'Math': 78, 'Science': 82, 'History': 80},
 'Emily': {'Math': 95, 'Science': 88, 'History': 92},
 'Sam': {'Math': 88, 'Science': 90, 'History': 85}}

subjects = ['Math', 'Science', 'History']
report_cards = {}
for student in students:
 grades_dict = grades[student]
 
 # retrieves the dictionary of subjects and grades 
 # for that student from the grades dictionary.
 total_grades = sum(grades_dict.values())
 average_grade = total_grades / len(subjects)
 report_cards[student] = {'Grades': grades_dict, 'Average': average_grade}
 #adds a report card entry for the student in the report_cards dictionary.
 #It includes the grades dictionary and the average grades
 
for x,y in report_cards.items():
 print(x,"->",y)
print()
# Printing the report cards
for student, report_card in report_cards.items():
#starts a loop that iterates over each student and 
# their corresponding report card in the report_cards dictionary.
 print(f"Report card for {student}:")
 for subject, grade in report_card['Grades'].items():
 # starts a loop that iterates over each subject and its corresponding grade 
 # in the grades dictionary of the report card.
  print(f"{subject}: {grade}")
 print(f"Average Grade: {report_card['Average']}")
 print() #adds a newline for formatting