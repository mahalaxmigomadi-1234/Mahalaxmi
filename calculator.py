a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before:", a, b)
print("Addition:", a + b)
print("Subtraction:", a - b)

a, b = b, a

print("After:", a, b)
print("Addition:", a + b)
print("Subtraction:", a - b)
