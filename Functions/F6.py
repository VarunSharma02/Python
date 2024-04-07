# Write a function that takes a list of numbers 
#as an argument and returns the sum of the squares 
#of those numbers.
def sum_squares(num):
    return sum(x**2 for x in num)
numbers=[1,2,3,4]
print(sum_squares(numbers))

