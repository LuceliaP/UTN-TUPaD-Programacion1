#----------------  Ejercicio 1  --------------------

print("Hola Mundo!")

#----------------  Ejercicio 2  --------------------

nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

#----------------  Ejercicio 3  --------------------

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
resi = input("Por ultimo, ingresa tu lugar de residencia actual: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {resi}")

#----------------  Ejercicio 4  --------------------
import math
radio = int(input("Ingrese el radio del circulo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"Dado el radio de {radio}, el perimetro es de {perimetro} y el area es de {area}")

#----------------  Ejercicio 5  --------------------

segundos = int(input("Ingrese una cantidad de segundos: "))
eq_minutos = segundos / 60
eq_horas = eq_minutos / 60
print ("El equivalente en horas es ", eq_horas)

#----------------  Ejercicio 6  --------------------

numero = int(input("Ingrese un numero: "))
print(f"La tabla del {numero} es: ")
print(f"{numero} X 1 = {numero * 1}")
print(f"{numero} X 2 = {numero * 2}")
print(f"{numero} X 3 = {numero * 3}")
print(f"{numero} X 4 = {numero * 4}")
print(f"{numero} X 5 = {numero * 5}")
print(f"{numero} X 6 = {numero * 6}")
print(f"{numero} X 7 = {numero * 7}")
print(f"{numero} X 8 = {numero * 8}")
print(f"{numero} X 9 = {numero * 9}")
print(f"{numero} X 10 = {numero * 10}")

#----------------  Ejercicio 7  --------------------

numero1 = int(input("Ingrese un numero entero distinto de cero: "))
numero2 = int(input("Ingrese otro numero entero distinto de cero: "))

print(f"{numero1} + {numero2} = {numero1 + numero2}")
print(f"{numero1} - {numero2} = {numero1 - numero2}")
print(f"{numero1} X {numero2} = {numero1 * numero2}")
print(f"{numero1} % {numero2} = {numero1 / numero2}")

#----------------  Ejercicio 8  --------------------

altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kgr: "))

indice_mc = peso /altura ** 2

print(f"Su indice de masa corporal es de: {indice_mc}")

#----------------  Ejercicio 9  --------------------

celsius = int(input("Ingrese la temperatura celsius a convertir: "))
fahrenheit = celsius * (9/5) + 32

print("La temperatura en fahrenheit es de: ", fahrenheit)

#----------------  Ejercicio 10  --------------------

nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print("El promedio es de: ", promedio)
