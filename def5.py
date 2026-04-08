def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

celsius = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La temperatura en Fahrenheit es: {fahrenheit}°F")