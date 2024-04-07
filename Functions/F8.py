# Define a function that takes a string and returns a new string with all 
#vowels converted to uppercase.

def string(str):
    vowels='aeiouAEIOU'
    return''.join(char.upper() if char in vowels else char for char in str)
text="heLLo World"
print(string(text))

# Write a function that accepts a tuple and a value, and returns 
# a new tuple with the value added at the end.
def add_to_tuple(t,value):
    return t+(value,)
my_tuple=(1,2,3,4)
value_to_added=5
print(add_to_tuple(my_tuple,value_to_added))

# Create a function that modifies a given list of names by removing any duplicates.
def duplicate(lst):
    return list(set(lst))
my_list=["Allu","Aman","Allu","Varun","Allu","Aman"]
print(duplicate(my_list))
