cost=float(input("Enter the amount"))
customer=input("You are a member (Yes/No)")
if cost>=100 and customer=="Yes" or customer=="yes":
 totalcost=cost-10/100
 print("total cost :",totalcost) 
else:
 print("Total cost:",cost)
  