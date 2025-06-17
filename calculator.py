def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    elif operator == '%':
        if num2 == 0:
            return "Error: Modulo by zero"
        return num1 % num2
    else:
        return "Invalid operator"

# Taking inputs from the user
try:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /, %): ")
    num2 = float(input("Enter the second number: "))

    result = calculator(num1, num2, operator)
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter numeric values.")
