while True:
    try:
        Number_1 = int(input("Enter Number One: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

while True:
    Operation = input("Enter the sign of operation you want to perform (+, -, *, /): ")
    if Operation in ["+", "-", "*", "/"]:
        break
    else:
        print("Invalid operation. Please enter one of the following: +, -, *, /")

while True:
    try:
        Number_2 = int(input("Enter Number Two: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if Operation == "+":
    print(f"{Number_1} + {Number_2} =", Number_1 + Number_2)
elif Operation == "-":
    print(f"{Number_1} - {Number_2} =", Number_1 - Number_2)
elif Operation == "*":
    print(f"{Number_1} * {Number_2} =", Number_1 * Number_2)
elif Operation == "/":
    if Number_2 != 0:
        print(f"{Number_1} / {Number_2} =", Number_1 / Number_2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Operation Not Found")
