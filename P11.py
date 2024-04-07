P=float(input("Enter the  principle amount (in dollars)"))
R=float(input("Enter the interest rate(in percentage):"))
n=float(input("Enter the time period of the loan (in years):"))
r=0 #r= monthly rate of interest 
r=(R/1200)
x=0 #x=value from the formula
x=(1+r)**(n*12)
M=(P*r*x)/(x-1)
print(f"Monthly payment: {M:.2f} dollars")
