l=[]
list=int(input("Number of items you want"))
for i in range(list):
    items=int(input(f"Enter items{i+1}:-"))
    l.append(items)
print("Final List:-",l)    