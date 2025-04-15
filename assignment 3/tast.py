def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def division(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a * b

def multiplication(a, b):
    return a * b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")

choice = input("Enter your choice (1/2/3/4): ")

if choice == "1":
    print(f"Result: {addition(num1, num2)}")

elif choice == "2":
    print(f"Result: {subtraction(num1, num2)}")

elif choice == "3":
    print(f"Result: {division(num1, num2)}")

elif choice == "4":
    print(f"Result: {multiplication(num1, num2)}")
