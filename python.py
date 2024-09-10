# Ejercicio 1

nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
print(f"Hola {nombre} {apellido}, ¡bienvenido!")


# Ejercicio 2
precio = 100
descuento = 0.15
precio_final = precio - (precio * descuento)
print(f"El precio con un 15% de descuento es: {precio_final}")


# Ejercicio 3
edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
    
    
    # Ejercicio 4
numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")


# Ejercicio 5
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
if num2 != 0:
    print(f"División: {num1 / num2}")
else:
    print("No se puede dividir por cero.")
    
    
    # Ejercicio 6
calificacion = float(input("Introduce tu calificación: "))
if calificacion >= 70:
    print("Aprobado")
else:
    print("Reprobado")



# Ejercicio 7
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
if num1 > num2:
    print(f"El número mayor es {num1}")
elif num2 > num1:
    print(f"El número mayor es {num2}")
else:
    print("Ambos números son iguales.")



# Ejercicio 8
nombre = input("Introduce tu nombre: ")
print(f"Bienvenido, {nombre}!")


# Ejercicio 9
numero = int(input("Introduce un número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")



# Ejercicio 10
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
promedio = (num1 + num2) / 2
print(f"El promedio es: {promedio}")


