is_vegetarian = input("Are you vegetarian? (yes/no): ").lower()
budget = float(input("Enter your budget: "))
time_available = int(input("Enter time available (minutes): "))
if is_vegetarian == "yes":
 if budget >= 10 and time_available >= 15:
  recommended_meal = "Vegetarian Burger"
 else:
  recommended_meal = "Salad"
else:
 if budget >= 15 and time_available >= 20:
  recommended_meal = "Chicken Burger"
 else:
  recommended_meal = "Fries"
print(f"We recommend: {recommended_meal}")
