student_scores={}
size=int(input("Enter the size of the dictionary"))
for i in range(size):
    key=input("Enter the  Student's name:") 
    value=int(input("Enter the Student's score between 0 to 100:"))
    student_scores[key]=value

highest_grade=-1
for grade in student_scores.values():
    if grade > highest_grade:
        highest_grade=grade

top_students=[student for student,grade in student_scores.items() if grade==highest_grade]        
print(f"The highest grade is:{highest_grade}")
print(f"The student(s) with the highest grade:{','.join(top_students)}")