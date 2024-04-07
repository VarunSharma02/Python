'''def modify_int(x):
 x += 10
 print("Inside the function:", x)
num = 5
modify_int(num)
print("Outside the function:", num)'''

'''def modify_string(s):
 s += " World!"
 print("Inside the function:", s)
greeting = "Hello"
modify_string(greeting)
print("Outside the function:", greeting)'''

'''def modify_tuple(t):
 # Tuples are immutable, so creating a new tuple
 t += (4, 5)
 print("Inside the function:", t)
coordinates = (1, 2, 3)
modify_tuple(coordinates)
print("Outside the function:", coordinates)'''

#Mutable Data Types:
'''def modify_list(lst):
 lst.append(4)
 lst[0] = 99
 print("Inside the function:", lst)
numbers = [1, 2, 3]
modify_list(numbers)
print("Outside the function:", numbers)'''

'''def modify_dict(d):
 d['new_key'] = 'new_value'
 print("Inside the function:", d)
my_dict = {'key1': 'value1', 'key2': 'value2'}
modify_dict(my_dict)
print("Outside the function:", my_dict)'''

'''def modify_set(s):
 s.add(4)
 print("Inside the function:", s)
my_set = {1, 2, 3}
modify_set(my_set)
print("Outside the function:", my_set)'''

'''def outer_function():
 # Outer function variable
 z = 30
 def inner_function():
  nonlocal z
 # Nonlocal variable
  z += 5
  print("Inside inner function:", z)
 inner_function()
 print("Inside outer function:", z)
outer_function()'''

# Global variable
'''global_var = 100
def modify_global_variable():
 global global_var
 global_var += 50
 print("Inside function:", global_var)
print("Before function:", global_var)
modify_global_variable()
print("After function:", global_var)

def Prime(num):
  if num==0 or num==1:
    return "Not Prime"
  for i in range(2,int(num**0.5)+1):
      if num%i==0:
         return "Not Prime"
  return "Prime" 

n=int(input()) 
re=Prime(n)
print(re)'''

'''def Leapyear(year):
    return "Leap Year"*((year%4==0 and year%100!=0) or (year%400==0)) or "Not a  leap year"

n=int(input())
re=Leapyear(n)
print(re)'''



