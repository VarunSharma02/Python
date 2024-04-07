# Write a function called calculate_factorial that takes a non-negative integer as input and returns its factorial.
def calculate_factorial(n):
 if n == 0 or n == 1:
  return 1
 else:
  return n * calculate_factorial(n - 1)
#If n is greater than 1, the function recursively calls itself with n - 1 and multiplies the result by n.
#For example, if you call calculate_factorial(5), it evaluates as follows:
#5!=5×4!=5×4×3!=5×4×3×2!=5×4×3×2×1!=5×4×3×2×1×0!
# Test the function
num = int(input("Enter a non-negative integer: "))
result_factorial = calculate_factorial(num)
print(f"The factorial of {num} is: {result_factorial}")