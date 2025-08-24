'''#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad_usuario = int(input("Ingrese su edad: "))

if edad_usuario >= 18:
    print("Es mayor de edad")
else:
    pass

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

nota_usuario = int(input("Ingrese su nota: "))

if nota_usuario >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:

edad_usu = int(input("Ingrese su edad: "))

if edad_usu < 12:
    print("Pertenece a la categoría Niño/a")
elif edad_usu >= 12 and edad_usu < 18:
    print("Pertenece a la categoría adolescente")
elif edad_usuario >= 18 and edad_usu < 30:
    print("Pertenece a la categoría adulto joven")
elif edad_usu > 30:
    print("Pertenece a la categoria adulto")
else:
    print("Ingrese una edad válida")'''

'''5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string. 

contrasenia = input("Ingrese una contraseña entre 8 y 14 caracteres: ")
longitud = len(contrasenia)

if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números (...)

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1,100) for i in range (50)]

mi_media = mean(numeros_aleatorios)
mi_mediana = median(numeros_aleatorios)
mi_moda = mode(numeros_aleatorios)

sesgo_positivo = False
sesgo_negativo = False
sin_sesgo = False

if mi_media > mi_mediana and mi_mediana > mi_moda:
    sesgo_positivo = True
elif mi_media < mi_mediana and mi_mediana < mi_moda:
    sesgo_negativo = True
elif mi_media == mi_mediana == mi_moda:
    sin_sesgo = True

print(f"El promedio es de {mi_media}, la mediana es {mi_mediana}, la moda es de {mi_moda}")    

print(f"El sesgo positivo es {sesgo_positivo}, el sesgo negativo es {sesgo_negativo} y la ausencia de sesgo es {sin_sesgo}")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

mi_frase = input("Ingrese una palabra o frase: ")

if mi_frase.endswith(("a", "e", "i", "o", "u")):
    mi_frase += "!"
else:
    pass

print(mi_frase)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee (...)

tu_nombre = input("Ingresa tu nombre: ")

print("Si queres tu nombre en mayusculas pulsa 1, si lo queres en letras minusculas pulsa 2 y si lo queres solo con la primera letra capital ingresa 3")
tu_eleccion = int(input("Ingresa la opcion que prefieres: "))

if tu_eleccion == 1:
    print(tu_nombre.upper())
elif tu_eleccion == 2:
    print(tu_nombre.lower())
elif tu_eleccion == 3:
    print(tu_nombre.title())
else:
    print("Elige una opcion valida")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# agnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:

mi_magnitud = int(input("Ingrese la magnitud del terremoto: "))

if mi_magnitud < 3:
    print("La magnitud del terremoto es muy leve")
elif mi_magnitud >=3 and mi_magnitud < 4:
    print("La magnitud del terremoto es leve")
elif mi_magnitud >= 4 and mi_magnitud < 5:
    print("La magnitud del terremoto es moderado")
elif mi_magnitud >= 5 and mi_magnitud < 6:
    print("La magnitud del terremoto es fuerte")
elif mi_magnitud >= 6 and mi_magnitud < 7:
    print("La magnitud del terremoto es muy fuerte")
else:
    print("La magnitud del terremoto es extremo")'''

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

from datetime import date

mi_hemisferio = input("En que hermisferio te encuentras? Coloca N por norte y S por sur ")
mi_mes = int(input("Ingresa el numero del mes en el que te encuentras, por ejemplo Enero = 1 "))
mi_dia = int(input("Que dia es hoy? Ingresa solo el dia, sin mes ni año"))




