l=list(map(int,input().split()))
even=[]
odd=[]
for i in range(0,len(l)):
    if i%2 != 0:
        even.append(l[i])
    else:
        odd.append(l[i])
print("Even Indexed:",even)
print("Odd Indexed:",odd)        
