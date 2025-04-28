# Solicitar al usuario que ingrese la temperatura en Celsius

celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Convertir Celsius a Fahrenheit (F = (C × 9/5) + 32)
fahrenheit = (celsius * 9/5) + 32

# Mostrar el resultado redondeado a 2 decimales
print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")