l=list(map(int,input().split()))
i=0
j=len(l)-1
flag=True
while i<j:
    if (l[i]!=l[j]):
        print("No")
        flag=False
        break
    i+=1
    j=j-1
if(flag==True):
    print("Yes")
   

