def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Taking input from the user
temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

# Conversion based on unit
if unit == "C":
    converted = celsius_to_fahrenheit(temp)
    print(f"{temp}°C is equal to {converted:.2f}°F")
elif unit == "F":
    converted = fahrenheit_to_celsius(temp)
    print(f"{temp}°F is equal to {converted:.2f}°C")
else:
    print("Invalid unit. Please enter 'C' or 'F'.")
