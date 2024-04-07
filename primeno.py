start = int(input("Enter starting number"))
end = int(input("Enter ending number"))
print("Prime numbers between", start, "and", end, "are:")
for num in range(start, end + 1):
 # all prime numbers are greater than 1
 #Prime numbers are defined as positive integers greater than 1.
 if num > 1:
  for i in range(2, num):
   if (num % i) == 0:
     #if statement checks if the current number num is divisible by i 
      # (i.e., num modulo i is zero). 
      # If this condition is true, it means num is not a prime number.
    break
     #If num is found to be divisible by i, 
      # the break statement is executed, which exits the inner for loop.
  else:
      #If the inner loop completes without finding any factors of num, 
     # the else block is executed. This means that num is a prime number.
    print(num)




