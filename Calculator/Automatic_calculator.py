# This is automatic no need to change the symbol like the before one 

num1 = float(input("Enter a number: " ))
method = input("Enter method: ")
num2 = float(input("Enter another number: "))

if method == "+":
    print(num1 + num2)
elif method == "-":
    print(num1 - num2)
elif method == "/":
    print(num1 / num2)
elif method == "*":
    print(num1 * num2)
else:
    print("Invalide method")
