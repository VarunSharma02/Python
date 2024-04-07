dict={}
size=int(input("Eneter the size of the dictionary"))
for i in range(size):
    key=input("Enter the  key:")
    value=input("Enter the value:")
    dict[key]=value  #or - user(update{key:value})

print("Resulting dictionary")
print(dict)