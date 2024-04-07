num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Perform arithmetic operations
operation = input("Enter the operation (+, -, /, %, //, **): ")
if operation == "+":
 result = num1 + num2
 print(f"Addition: {num1} + {num2} = {result}")
elif operation == "-":
 result = num1 - num2
 print(f"Subtraction: {num1} - {num2} = {result}")
elif operation == "/":
 if num2 != 0:
  result = num1 / num2
  print(f"Division: {num1} / {num2} = {result}")
 else:
  print("Division by zero is not allowed.")
elif operation == "%":
 if num2 != 0:
  result = num1 % num2
  print(f"Modulus: {num1} % {num2} = {result}")
 else:
  print("Modulus by zero is not allowed.")
elif operation == "//":
 if num2 != 0:
  result = num1 // num2
  print(f"Floor Division: {num1} // {num2} = {result}")
 else:
  print("Floor division by zero is not allowed.")
elif operation == "**":
 result = num1 ** num2
 print(f"Exponentiation: {num1} ** {num2} = {result}")
else:
 print("Invalid operation.")


        
