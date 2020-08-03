# Small Exercise 6. Celsius to Fahrenheit

# Prompt the user for a number in degrees Celsius, and convert the value to degrees in Fahrenheit and display it to the user.

def degree_conversion():
    temp_in_c = int(input("What celcius temperature do you want to convert? "))
    return(temp_in_c * 9 / 5) + 32
print(degree_conversion())

temperature = input("Temperature in C?")
fahrenheit = (int(temperature) * 9/5) + 32
print(fahrenheit)