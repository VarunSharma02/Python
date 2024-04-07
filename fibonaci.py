n=int(input("Enter the no."))
if(n==0 or n==1):
  print(n)
else:
  i=2
  a=0
  b=1
  while(i<=n):
   c=a+b
   a=b
   b=c
   i+=1
  print(c)   
