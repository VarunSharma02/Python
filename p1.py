age=int(input("Enter your age"))
if age<=3:
 print("You can watch for free")
elif age>=4 or age<=12:
 print("You have to pay $10")
elif age>=13 or age<=17:
 print("You have to pay $15")
else:
 print("You have to pay $20")
