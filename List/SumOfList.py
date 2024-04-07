element=int(input("Number of items you want"))
l1=[0]*element
for  i in range(element):
    items=int(input(f"Enter item{i+1}:-"))
    l1[i]=items
print("Your list:-",l1)
# to find the sum of all items of the list
sum=0
for i in l1:
    sum+=i
print("The sum of the elements of your list:-",sum)        
# to find the maximum number in the list
max=l1[0]
for i in l1:
    if i>max:
        max=i
print("Largest element in your list:-",max)        