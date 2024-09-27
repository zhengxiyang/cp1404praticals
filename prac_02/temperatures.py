def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius_value = 25
fahrenheit_result = celsius_to_fahrenheit(celsius_value)
print(f"{celsius_value} degrees Celsius is {fahrenheit_result:.2f} degrees Fahrenheit")

fahrenheit_value = 77
celsius_result = fahrenheit_to_celsius(fahrenheit_value)
print(f"{fahrenheit_value} degrees Fahrenheit is {celsius_result:.2f} degrees Celsius")
