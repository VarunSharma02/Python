fruits = {"apple": 2,"banana": 5,"orange": 3,"grape": 7}
print("Fruits with quantities > 4:")
for fruit,quantity in fruits.items():
    if quantity>4:
        print(f"{fruit}:{quantity}")

# Doubling the quantity of oranges
fruits["oranges"]*=2



