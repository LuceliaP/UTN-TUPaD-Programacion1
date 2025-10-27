
"""

1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
"""

#Definimos la función
def factorial_rec(numero):
  #definimos el case base
  if numero == 0:
    return 1
  #definimos el paso recursivo
  else:
    return numero * factorial_rec(numero -1)

#solicitamos un número al usuario
tu_num = int(input("Ingrese el número límite: "))

#utilizamos un for para mostrar el factorial de todos los números, sumamos 1 porque in range no incluye el último indice
for i in range(1, tu_num +1):
  print(f"Para el número {i} el factorial es {factorial_rec(i)}")

"""2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
"""

def fibonacci_rec(posicion_fr):
  if posicion_fr == 0:
    return 0
  elif posicion_fr ==1:
    return 1
  else:
    return fibonacci_rec(posicion_fr -1) + fibonacci_rec(posicion_fr -2)

posicion = int(input("Ingrese un número: "))
for i in range(posicion):
  print(f"Para el número {i} el calculo Fibonacci es {fibonacci_rec(i)}")

"""3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛
𝑚 = 𝑛 ∗ 𝑛
(𝑚−1)
. Prueba esta función en un
algoritmo general.
"""

def potencia_rec(base, exponente):
  if exponente == 0:
    return 1
  else:
    return base * potencia_rec(base, exponente -1)

from math import pi
def calcular_area_circ(radio):
  return pi * potencia_rec(radio, 2)

tu_radio = float(input("Ingrese el radio de la circunferencia a calcular: "))
print(f"El area de la circunferencia con radio {tu_radio} es {calcular_area_circ(tu_radio)}")

"""4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.

"""

def convertir_bin(numero):
  if numero <2:
    return str(numero)
  else:
    return (convertir_bin(numero//2))+str(numero % 2)

print(convertir_bin(10))

"""5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
 Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed()
"""

def es_palindromo(frase):
  if len(frase) <= 1:
    return True
  elif frase[0] != frase[-1]:
    return False
  else:
    return es_palindromo(frase[1:-1])

print(es_palindromo("reconocer"))
print(es_palindromo("amor"))

"""6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
 Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)

"""

def suma_digitos(num):
  if num<10:
    return num
  else:
    ultimo = num % 10
    return ultimo + suma_digitos(num // 10)

print(suma_digitos(35155))

"""7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide
"""

def contar_bloques(num):
  if num == 1:
    return 1
  else:
    return num + contar_bloques(num-1)

print(contar_bloques(3))

"""Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
"""

def contar_digito(numero,digito):
  if numero < 10:
    return 1 if numero == digito else 0
  else:
    ultimo = numero % 10
    if ultimo == digito:
      return 1 + contar_digito(numero // 10, digito)
    else:
      return contar_digito(numero // 10, digito)


print(contar_digito(35155879, 5))