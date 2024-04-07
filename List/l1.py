# Initialize the list
numbers = [1, 3, 5, 7, 9, 11, 13, 15]
# Access and print element at index 3
print(f"Element at index 3: {numbers[3]}")
# Access and print the last element
print(f"Last element: {numbers[-1]}")
# Access and print sublist from index 1 to 4 (inclusive)
sublist = numbers[1:5]
print(f"Sublist from index 1 to 4: {sublist}")
# Change the value at index 2 to 10
numbers[2] = 10
print(f"Modified list after changing element at index 2: {numbers}")
# Append the value 20 to the end of the list
numbers.append(20)
print(f"List after appending 20: {numbers}")
# Remove the element at index 0
del numbers[0]
print(f"List after removing element at index 0: {numbers}")
# Insert the value 5 at index 1
numbers.insert(1, 5)
print(f"List after inserting 5 at index 1: {numbers}")
# Print the final list
print(f"Final List: {numbers}")
