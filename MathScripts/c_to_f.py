def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

c_temp = 25
f_temp = celsius_to_fahrenheit(c_temp)
print(f"{c_temp}°C is equivalent to {f_temp}°F")
