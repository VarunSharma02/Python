# Write a function called is_palindrome that takes a string as input and returns 
#True if the string is a palindrome (reads the same backward as forward), and 
#False otherwise.

def is_palindrome(s):
 s = s.lower().replace(" ", "")
 return s == s[::-1]
# Test the function
input_str = input("Enter a string: ")
if is_palindrome(input_str):
 print("It's a palindrome!")
else:
 print("It's not a palindrome.")
