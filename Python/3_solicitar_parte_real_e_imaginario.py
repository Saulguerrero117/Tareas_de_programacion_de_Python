# Solicitar partes real e imaginaria de ambos números
6
print("Ingresa el primer número complejo:")
real1 = float(input("Parte real: "))
imag1 = float(input("Parte imaginaria: "))

print("\nIngresa el segundo número complejo:")
real2 = float(input("Parte real: "))
imag2 = float(input("Parte imaginaria: "))

# Crear números complejos y sumarlos
complejo1 = complex(real1, imag1)
complejo2 = complex(real2, imag2)
resultado = complejo1 + complejo2

print(f"\nResultado: {complejo1} + {complejo2} = {resultado}")