def fahrenheit_to_celsius(fahrenheit): # Function used to convert F to C
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

f_temp = 98.6  # Example of Fahrenheit temperature
c_temp = fahrenheit_to_celsius(f_temp) # how celcius is defined in the funtion
print(f"{f_temp}°F is equal to {c_temp:.2f}°C")
