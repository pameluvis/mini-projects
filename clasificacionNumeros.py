def clasificacion(num):
    clasificacion = "Pequeño" if num < 5 else "Mediano" if num < 10 else "Grande"
    return clasificacion

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

print(f"Número {num1}: {clasificacion(num1)}")
print(f"Número {num2}: {clasificacion(num2)}")
print(f"Número {num3}: {clasificacion(num3)}")