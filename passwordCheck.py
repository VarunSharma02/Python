# check for strong password entered by the user. Use isalpa(), isdigit(), isspace() function in python
# Conditions to check:-
# 1. Password atleast 12 characters (comprises of alphabets, digits and special characters)
# 2. Atleast one uppercase and lowercase letter
# 3. Atleast one digit and special characters (!,@,#,%,? etc)
#Continue the program until user enter a valid strong password
while True:
# Get password from user
 password=input("Enter your password:") 
 if len(password)<12: # Condition 1: At least 12 characters
  print("Password should be atleast 12 characters")
  continue
 else:
  has_uppercase = False
  has_lowercase = False
  has_digit = False
  has_special = False
  has_space = False
  for char in password:
   if char.isalpha():
    if char.isupper():
     has_uppercase=True
    elif char.islower():
     has_lowercase=True
   elif char.isdigit():
    has_digit=True
   elif char.isspace():
    has_space=True
   else:
    has_special=True
  if has_uppercase and has_lowercase and has_digit and has_special:
   print("Password is strong")
   break
  else:
   print("Password is not strong.Please try again")     
     
     



  