l=list(map(int,input().split()))
temp=l[len(l)-1]
i=len(l)-2
while i>=0:
    l[i+1]=l[i]
    i-=1
l[0]=temp
print(l)