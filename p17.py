N1 = int(input("enter lower bound"))
N2 = int(input("enter upper bound"))
for n in range(N1,N2+1):
 if n>1:
    flag=True
    for i in range(2,n):
        if(n%i==0):
            flag=False
            break
    if(flag==True):
        print(n)    

        #or you can use the following function

'''N1 = int(input("enter lower bound"))
N2 = int(input("enter upper bound"))	
for num in range(N1, N2 + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)'''

