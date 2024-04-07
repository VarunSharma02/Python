num1=int(input("Enter the  starting number"))
num2=int(input("enter the ending number"))
even=0
odd=0 
for i in range(num1,num2+1):
    if(i%2==0):
        even+=i
    else:
        odd+=i
print(f"Sum of even no. b/w {num1} and {num2}:",even)
print(f"Sum of odd no. b/w {num1} and {num2}:",odd)        


    