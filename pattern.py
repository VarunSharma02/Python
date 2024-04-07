no_of_lines=int(input("Enter the lines"))

for i in range(no_of_lines,0,-1):
    print("*"*i)


    # or you can use the following function
n=int(input("Enter the no."))
for row in range(n,0,-1):
    for col in range(row,0,-1):
        print("*", end="")
    print()   