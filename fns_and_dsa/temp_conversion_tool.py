FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    convo = (fahrenheit - 32 )* FAHRENHEIT_TO_CELSIUS_FACTOR
    print(convo)

convert_to_celsius(100)
print(FAHRENHEIT_TO_CELSIUS_FACTOR)