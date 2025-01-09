FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32 ) * FAHRENHEIT_TO_CELSIUS_FACTOR
    

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    

temp = (input("Enter the temperature to convert: "))


if temp == str:
    print("Invalid temperature. please enter a numeric value")

elif temp == int:
    
    temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

    if temp_unit == "F":
    
        print(f"{temp}°{temp_unit} is {convert_to_celsius(temp)}°C")
    elif temp_unit == "C":
    
        print(f"{temp}°{temp_unit} is {convert_to_fahrenheit(temp)}°F")

