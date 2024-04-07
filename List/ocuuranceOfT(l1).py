'''l=list(map(int,input().split()))
print(l)'''

n=int(input("Enter the number of elements"))
l=list(map(int,input().split())) #Enter the element in a single row to make a list
T=int(input("Enter the element to be checkesd"))
for i in range(n):
    if(l[i]==T):
        print(i)
        break
if(i==n):
    print(-1)