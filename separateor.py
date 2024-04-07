user_input = input("Enter the string ")
data_alphabets = ""
data_digits = ""
for i in user_input:
 if i.isalpha():
  data_alphabets+=i
 elif i.isdigit():
  data_digits+=i
print(f"All the digits are :- {data_digits}")
print(f"All the alphabets are:- {data_alphabets}")






