'''l=list(map(int,input().split()))
i=0
j=len(l)-1
while i<j:
    temp=l[i]
    l[i]=l[j]
    l[j]=temp
    i+=1
    j-=1
print(l) '''

limit=int(input("Enter the limit"))
num1=0
num2=1
num3=0
l=[]
l.append(num1)
l.append(num2)
for i in range(3, limit+1):
    num3=num1+num2
    l.append(num3)
    num1=num2
    num2=num3
print(l, end=" ")