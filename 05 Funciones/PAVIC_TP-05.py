# --------------- 1 --------------

#Definicion de funciones

def imprimir_hola_mundo():
  print("Hola Mundo!")

#Programa principal
imprimir_hola_mundo()

# --------------- 2 --------------

#Definicion de funciones

def saludar_usuario(nombre):
  print(f"Hola, {nombre}!")

#Programa principal

tu_nombre = input("Ingresa tu nombre: ")
saludar_usuario(tu_nombre)

# --------------- 3 --------------
#Definicion de funciones

def informacion_personal(nombre, apellido, edad, ciudad):
  print(f"Soy {nombre} {apellido}, tengo {edad} años, vivo en {ciudad}.")

#Programa principal

tu_nombre = input("Ingresa tu nombre: ")
tu_apellido = input("Ingresa tu apellido: ")
tu_edad = int(input("Ingresa tu edad: "))
tu_ciudad = input("Ingresa tu ciudad de residencia: ")

informacion_personal(tu_nombre, tu_apellido, tu_edad, tu_ciudad)

# --------------- 4 --------------

#Definicion de funciones
import math
def calcular_area_circulo(radio):
  area = math.pi * radio**2
  return area

def calcular_perimetro_circulo(radio):
  perimetro = 2 * math.pi * radio
  return perimetro

def formatear_resultados(resultado):
  resultado_2d = round(resultado,2)
  return resultado_2d

#Programa principal
tu_radio = float(input("Ingresa el radio del circulo a calcular: "))
print(f"El area es {formatear_resultados(calcular_area_circulo(tu_radio))}")
print(f"El perimetro del circulo es {formatear_resultados(calcular_perimetro_circulo(tu_radio))}")

# --------------- 5 --------------

#Definicion de funciones

def segundos_a_horas(segundos):
  minutos = segundos /60
  horas = minutos /60
  return horas

#Programa principal

tus_segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"Los segundos ingresados son {segundos_a_horas(tus_segundos)} horas")

# --------------- 6 --------------

def tabla_multiplicar(numero):
  for i in range(1,11):
    print(f"{numero} x {i} = {i * numero}")

tu_numero = int(input("Ingresa un numero: "))
tabla_multiplicar(tu_numero)


# --------------- 7 --------------

#Definicion de funciones
def operaciones_basicas(a, b):
  una_tupla = (a+b, a-b, a*b, a/b)
  return una_tupla

#Porgrama principal

tu_a = int(input("Ingresa un numero: "))
tu_b = int(input("Ingresa otro numero: "))
print(f"La tupla es: {operaciones_basicas(tu_a, tu_b)}")
print(f"La suma del primero con el segundo es {operaciones_basicas(tu_a, tu_b)[0]}")
print(f"La resta del primero con el segundo es {operaciones_basicas(tu_a, tu_b)[1]}")
print(f"La multiplicacion del primero con el segundo es {operaciones_basicas(tu_a, tu_b)[2]}")
print(f"La division del primero con el segundo es {operaciones_basicas(tu_a, tu_b)[3]}")


# --------------- 8 --------------


def calcular_IMC(peso, altura):
  imc = peso / altura**2
  return imc

tu_peso = float(input("Ingresa tu peso en kilogramos: "))
tu_altura = float(input("Ingresa tu altura en metros: "))
print(f"Tu IMC es {round(calcular_IMC(tu_peso, tu_altura), 2)}")

# --------------- 9 --------------

def celsius_a_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

tu_celsius = float(input("Ingresa la temperatura en grados Celsius: "))
print(f"La temperatura en grados Fahrenheit es {round(celsius_a_fahrenheit(tu_celsius), 2)}")

# --------------- 10 --------------

def calcular_promedio(a, b, c):
  promedio = (a+b+c)/3
  return promedio

nota_a = float(input("Ingresa la primera nota: "))
nota_b = float(input("Ingresa la segunda nota: "))
nota_c = float(input("Ingresa la tercera nota: "))

print(f"El promedio de las notas es {round(calcular_promedio(nota_a, nota_b, nota_c), 2)}")