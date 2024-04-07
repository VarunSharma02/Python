# Write functions for basic mathematical operations:
# Addition
# Subtraction
# Multiplication
# Division
# Each function should take two parameters and return the result.

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b!=0:
        return a / b
    else:
        print(f"{a} is not divisible by {b} ")
a=int(input("Enter first argument"))
b=int(input("Enter second argument"))
print("Sum:",add(a, b))
print("Subtract:",sub(a, b))
print("Product",mul(a, b))
print("Divisble",div(a, b))
      