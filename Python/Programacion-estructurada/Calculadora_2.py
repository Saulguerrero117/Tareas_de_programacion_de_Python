#4-Crear una calculadora usando bibliotecas

import math

# Menú de operaciones
print("Calculadora Avanzada")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Potencia")
print("6. Raíz cuadrada")

# Pedir al usuario que elija una operación
opcion = input("Seleccione una operación (1/2/3/4/5/6): ")

# Para suma, resta, multiplicación y división, se necesitan dos números
if opcion in ["1", "2", "3", "4", "5"]:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == "1":
        print(f"Resultado: {num1 + num2}")
    elif opcion == "2":
        print(f"Resultado: {num1 - num2}")
    elif opcion == "3":
        print(f"Resultado: {num1 * num2}")
    elif opcion == "4":
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("Error: No se puede dividir entre cero.")
    elif opcion == "5":
        print(f"Resultado: {math.pow(num1, num2)}")

# Para raíz cuadrada, solo se necesita un número
elif opcion == "6":
    num = float(input("Ingrese el número para sacar la raíz cuadrada: "))
    if num >= 0:
        print(f"Resultado: {math.sqrt(num)}")
    else:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
else:
    print("Opción no válida.")


           