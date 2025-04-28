# Solicitar dos números al usuario

try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    # Operaciones básicas
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    
    # Mostrar resultados
    print(f"\nResultados:")
    print(f"Suma: {num1} + {num2} = {suma}")
    print(f"Resta: {num1} - {num2} = {resta}")
    print(f"Multiplicación: {num1} × {num2} = {multiplicacion}")
    
    # Manejar división (evitando división por cero)
    if num2 != 0:
        division = num1 / num2
        print(f"División: {num1} ÷ {num2} = {division:.2f}")  # Redondeado a 2 decimales
    else:
        print("División: No es posible dividir entre cero (∞)")
        
except ValueError:
    print("Error: Ingresa números válidos (p.ej., 5 o 3.14)")