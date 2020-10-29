# This is more fun to play with it will tell your name 

user_name = input("Enter your name: ")
print("Nice name " + user_name)

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
    
    
print("This is your answer " + user_name)
