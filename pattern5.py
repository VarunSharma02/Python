n=int(input("Enter the number"))
for row in range(1,n+1):
    for col in range(1,n-row+1):
        print(" ",end=" ")
    for star in range(n-row+1,n+1):
        print("*",end=" ")
    print()        