#371-> 3**3+7**3+1**3=371(Armstrong no.)
user_input=int(input("Enter the no. to be checked"))
num_of_digits=len(str(user_input))
sum_of_cubes=0
temp=user_input

while temp>0:
    digit=temp%10
    sum_of_cubes+=digit**num_of_digits
    temp //=10
if(user_input==sum_of_cubes):
    print(f"{user_input} is a armstrong number  ")
else:
    print(f" {user_input} is not a armstrong number ")        
