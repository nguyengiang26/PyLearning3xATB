try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ValueError as ve:
    print(ve)
except ZeroDivisionError as zde:
    print(zde)
else:
    print("Result:", result)
finally:
    print("Program execution completed.")
