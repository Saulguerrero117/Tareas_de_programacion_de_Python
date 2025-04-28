# Programa para determinar si un número es par o impar
try:
    numero = int(input("Ingresa un número entero: "))
    
    if numero % 2 == 0:
        print(f"El número {numero} es par 🟦")
    else:
        print(f"El número {numero} es impar 🟧")
        
except ValueError:
    print("Error: Debes ingresar un número entero válido (ej. 3, -8 o 0)")