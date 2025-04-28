#3-Crear una calculadora usando funciones

# Definir las funciones para cada operación
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero."

# Menú de operaciones
print("Calculadora")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

# Pedir al usuario que elija una operación
opcion = input("Seleccione una operación (1/2/3/4): ")

# Pedir los números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Realizar la operación correspondiente
if opcion == "1":
    resultado = sumar(num1, num2)
    print(f"El resultado de la suma es: {resultado}")
elif opcion == "2":
    resultado = restar(num1, num2)
    print(f"El resultado de la resta es: {resultado}")
elif opcion == "3":
    resultado = multiplicar(num1, num2)
    print(f"El resultado de la multiplicación es: {resultado}")
elif opcion == "4":
    resultado = dividir(num1, num2)
    print(f"El resultado de la división es: {resultado}")
else:
    print("Opción no válida.")
