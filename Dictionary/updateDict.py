student_scores={}
size=int(input("Eneter the size of the dictionary"))
for i in range(size):
    key=input("Enter the  key:") # key=John,Jane,Bob,Alice
    value=input("Enter the value:") # value=85,90,75,95
    student_scores[key]=value  #or - user(update{key:value})
print(student_scores)

student_scores["Sam"]=80
print(student_scores)
student_scores["Bob"]=80
del student_scores["Jane"]

for name,score in student_scores.items():
 print(f"{name}: {score}")


