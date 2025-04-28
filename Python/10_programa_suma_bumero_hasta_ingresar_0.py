# Programa para sumar números hasta que se ingrese 0

suma = 0  # Inicializar la suma en 0

print("Ingresa números para sumar (ingresa 0 para terminar):")

while True:
    try:
        numero = float(input("Número: "))  # Solicitar número al usuario
        
        if numero == 0:
            break  # Salir del bucle si se ingresa 0
        
        suma += numero  # Acumular la suma
        
    except ValueError:
        print("¡Error! Ingresa un número válido.")

# Mostrar resultado
print(f"\nLa suma total es: {suma}")