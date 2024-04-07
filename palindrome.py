string=input("Enter any string")
if string==string[::-1]:
    print("String is a palindrome")
else:
    print("String is not a palindrome")    
#or you can use
"""string=input("Enter any string")
reversed_string=" ".join(reversed(string))
if string==reversed_string:
    print(f"'{string}'is a palindrome")
else:
    print(f"'{string}'is a palindrome")"""


