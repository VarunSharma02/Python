def fac(t):
    ans=1
    for i in range(1,t+1):
        ans=ans*i
    return ans

n=int(input(f"Enter the value of n:"))
r=int(input("Enter the value of r:"))
c=fac(n)/(fac(n-r)*fac(r))
p=fac(n)/(fac(n-r))
print(f"The combination of {n} and {r} is ",c)
print(f"The permutation of {n} and {r} is ",p)   
    