#Solicitar número al usuario con manejo de errores

try:
    numero = float(input("Ingresa un número: "))
    
    # Determinar el tipo de número
    if numero > 0:
        print(f"El número {numero} es positivo ➕")
    elif numero < 0:
        print(f"El número {numero} es negativo ➖")
    else:
        print("El número es cero (0) ⚪")
        
except ValueError:
    print("Error: Debes ingresar un número válido (ej. 5, -3.2 o 0)")