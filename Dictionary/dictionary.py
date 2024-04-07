'''student={ "Roll no" :28587358257, "Name" :["Varun","Aman"], "eyepiece":"blue"}
print(student)
print(len(student))
print(type(student))
print(student["Name"]) #RAHUl


employ=dict(name="Survey", Salary=35000, age=21)
print(employ)
check=student.get("Name")
print(check)

print(student.keys())
print(student.values())

student["year"]=2023
print(student)
student.update({"Blood group":"A+"})
print(student)

if "blue" in student.values():
    print("Found")'''

'''thisdict={"brand":"Ford","model":"Mustang","Year":"1964"}
thisdict.pop("model")
print(thisdict)'''

'''thisdict={"brand":"Ford","model":"Mustang","Year":"1964"}
thisdict.popitem()
print("My Data",thisdict)'''

'''thisdict={"brand":"Ford","model":"Mustang","Year":"1964"}
del thisdict["model"]
print(thisdict)'''

'''thisdict={"brand":"Ford","model":"Mustang","Year":"1964"}
del thisdict
print(thisdict)'''

'''thisdict={"brand":"Ford","model":"Mustang","Year":"1964"}
thisdict.clear()
print(thisdict)'''


'''myStudent={
    "stud1":{"name":"Sachin","year":2004},
    "stud2":{"name":"Laxman","year":2007}, 
    "stud3":{ "name":"Ram","year":2011}}
print(myStudent)
print("----------------------------------------------------------------")
for x in myStudent:
    print(x)
print("----------------------------------------------------------------")
print(myStudent["stud1"]["name"])    

print("----------------------------------------------------------------")

for x,y in myStudent.items():
 print(x,y)
 print("----------------------------------------------------------------")'''

def func(num):
    num=500
    num=num+3
    print(num)
num=100
func(num)    
