inventory = {'apple':10,'banana':5, 'orange':8,'grape':3}
inventory["apple"]+=2
print(inventory)

if "banana" in inventory:
    print("Yes Available")
else:
    print("Not found") 

inventory["grape"]-=1

total_items=sum(inventory.values())
print(total_items)
