def safe_divide(numerator, denominator):
    try:
        result = numerator /denominator
        print(f"The result of the division is {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Please enter numeric values only.")
    except ValueError:
        print("Error: Please enter numeric values only.")

