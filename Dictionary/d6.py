s=input(" Enetr the string") #"geeksforgeeks"
d={}
k=int(input("Enter the range of repetion:"))
for i in s:
 if i in d:
  d[i]=d[i]+1
 else:
  d[i]=1
print(d)  
ans=""  
for i in s:
 if(d[i]<k):
  ans=ans+i
print(ans)

