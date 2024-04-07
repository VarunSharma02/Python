n=int(input("Enter any number"))
count=0
for i in range(1,n+1):
    if(n%i==0):
     count+=1
if(count==2):
   print("Prime No.")
else:
   print("Not a prime No.")   

