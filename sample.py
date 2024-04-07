"""newlist=["Abhishek","Pratham","Varun"]
mydata=newlist.copy()
print(mydata)
print("------------------------------------------")
newlist=["Varun","varun","vArUn"]
myData=list(newlist)
print(myData)
print("--------------------------------------------------")


myList=["S1","S2","S3","S4"]
del myList[0]
print("--------------------------------------------------")
mylist=[1,5,8,27,56,10]
mylist.sort()
print(mylist)
print("--------------------------------------------------")
list=["apple","banana","cherry"]
[print(x) for x in list ]
print("--------------------------------------------------")
l1=[x**2 for x in range(5)]
print(l1)
print("--------------------------------------------------")
l2=[x for x in range(10) if x%2==0]
print(l2)
print("--------------------------------------------------")
result=['Pass' if score>=60 else 'Fail' for score in [75,30,65,80]]
print(result)"""
""""
name="Varun"
message=("My name is %s")%name
print(message)"""


"""n=int(input().strip())
if n%2==0:
    if n>=2 and n<=5:
        print("Not Weird")
    elif n>=6 and n<=20:
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")  """

"""a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b) """

"""n=int(input())
for i in range(0,n):
 print(i**2)"""

# to join by - alphabet
"""a=input()
a=a.split(" ")
a="-".join(a)
print(a)"""

"""n1=int(input())
n2=int(input())
print(n1*n2)"""

#check valentine match
"""X=int(input())
Y=int(input())
if  X^Y==X+Y:
    print("Valentine Match")
else:
    print("None")"""  

#floor and ceil program:
"""import math
n=float(input())
n1=math.floor(n)
n2=math.ceil(n)
print(f"{n1:.6f}")
print(f"{n2:.6f}")"""

"""import re

s1=" The quick brown fox jumped over the lazy dog"
pattern=r"fox"
replacement="bear"
s2=re.sub(pattern,replacement,s1,re.IGNORECASE)
print(s2)"""

"""n=int(input("Enter the number"))
sum=0
for i in range(1,n+1):
    if i%2==0 and i%3==0: 
        sum+=i
print("The Sum of the numbers:-",sum)    """

# To count the number of vowel
'''sentence=input("Enter the sentence")
vowels="aeiouAEIOU"
vowels_count=0
for char in sentence:
    if char in vowels:
        vowels_count+=1
print("Number of vowels:",vowels_count)'''

'''numbers=[int(x) for x in input("Enter the integers separated by spaces").split()]
result=[x**2 for x in numbers if x%2==0 ]
print(" ".join([str(x) for x in result])) '''

   