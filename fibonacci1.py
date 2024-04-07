"""limit=int(input("Enter the limit"))
num1=0
num2=1
num3=0
print(num1, end=" ")
print(num2, end=" ")

for i in range(3, limit+1):
    num3=num1+num2
    print(num3, end=" ")
    num1=num2
    num2=num3

# Print Fibonacci series in list using range
limit=int(input("Enter the limit"))
num1=0
num2=1
num3=0
l=[]
l.append(num1)
l.append(num2)
for i in range(3, limit+1):
    num3=num1+num2
    l.append(num3)
    num1=num2
    num2=num3
print(l, end=" ")"""

#Using class and function:
class Fibonacci:
    def __init__(self, n):
        self.n = n

    def generate_series(self):
        fib_sequence = [0, 1]
        if self.n <= 2:
            return fib_sequence[:self.n]
        else:
            for i in range(2, self.n):
                next_fib = fib_sequence[-1] + fib_sequence[-2]
                fib_sequence.append(next_fib)
            return fib_sequence[:self.n]

n = int(input())

if n <= 0:
    print("Please enter a positive integer.")
else:
    fib_instance = Fibonacci(n)
    print(fib_instance.generate_series())