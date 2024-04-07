n=int(input("Enter any number"))
flag=True
for i in range(2,n):
    if(n%i==0):
        print("Not a prime no.")
        flag=False
        break
if(flag==True):
    print("Prime No.")    