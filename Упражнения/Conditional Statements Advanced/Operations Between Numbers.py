n1 = int(input())
n2 = int(input())
operation = input()
result = 0

if operation == "+":
    result = n1 + n2
elif operation == "-":
    result = n1 - n2
elif operation == "*":
    result = n1 * n2
elif operation == "/" and n2 != 0:
    result = n1 / n2
    print(f"{n1} {operation} {n2} = {result:.2f}")
elif operation == "%" and n2 != 0:
    result = n1 % n2
    print(f"{n1} {operation} {n2} = {result}")

if (operation == "/" or operation == "%") and n2 == 0:
    print(f"Cannot divide {n1} by zero")

if (operation == "+" or operation == "-" or operation == "*") and result % 2 == 0:
    print(f"{n1} {operation} {n2} = {result} - even")
elif (operation == "+" or operation == "-" or operation == "*") and result % 2 != 0:
    print(f"{n1} {operation} {n2} = {result} - odd")