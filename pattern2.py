n=int(input("Enter the no."))
row=1
for row in range(1,n-row+1):
    for space in range(1,n-row+1):
        print(" ",end="")
    print()    
