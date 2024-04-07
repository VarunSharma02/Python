word = input("Enter the password for your profile ")
num_letters,num_digits,num_special_chars,num_space = 0,0,0,0
# num_letters = 0
# num_digits = 0
# num_special_chars = 0
# num_space = 0
for pw in word:
 if pw.isalpha():
  num_letters += 1
 elif pw.isdigit():
  num_digits += 1
 elif pw.isspace():
  num_space +=1
 else:
  num_special_chars += 1
print(f"Number of letters: {num_letters}")
print(f"Number of digits: {num_digits}")
print(f"Number of spaces: {num_space}")
print(f"Number of special characters: {num_special_chars}")
while True:
 # Get password from user
 password = input("Enter your password: ")
 # Condition 1: At least 12 characters
 if len(password) < 12:
  print("Password should be at least 12 characters long.")
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
     has_uppercase = True
    elif char.islower():
     has_lowercase = True
   elif char.isdigit():
    has_digit = True
   elif char.isspace():
    has_space = True
   else:
    has_special = True
 # Conditions 2, 3, and 4
  if has_uppercase and has_lowercase and has_digit and has_special:
   print("This is a strong password!")
   break
  else:
   print("This is not a strong password. Please try again.")


 