
"""

1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""

mi_diccionario = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
mi_diccionario["Naranja"] = 1200
mi_diccionario["Manzana"] = 1500
mi_diccionario["Pera"] = 2300
print(mi_diccionario)

"""2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""

mi_diccionario["Banana"] = 1330
mi_diccionario["Manzana"] = 1700
mi_diccionario["Melón"] = 2800

print(mi_diccionario)

"""3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
"""

mi_lista = list(mi_diccionario.keys())
print(mi_lista)

"""4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
"""

guia_telefonica = {}

for i in range(2):
  nombre = (input("Ingrese el nombre: ")).title()
  telefono = input("Ingrese el teléfono: ")
  guia_telefonica[nombre] = telefono

while True:
  print("**** Guia Telefonica ****")
  print("Ingrese 1 para consultar o 2 para salir")
  opcion = input("Ingrese la opcion deseada: ")
  if opcion == "1":
    buscar_nombre = (input("Ingrese el nombre a buscar: ")).title()
    if buscar_nombre not in guia_telefonica:
      print("El nombre buscado no se encuentra en la guia")
    else:
      print(f"El teléfono de {buscar_nombre} es {guia_telefonica[nombre]}")
  elif opcion == "2":
    break
  else:
          print("Elija una opción válida")

"""5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.

"""

frase = input("Ingresa una frase: ")
palabras = frase.split()
set_palabras = set(palabras)
print(f"Palabras unicas: {set_palabras}")

dic_palabras = {}
for i in palabras:
  dic_palabras[i] = palabras.count(i)
print(f"Recuento: {dic_palabras}")

"""6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.

"""


lista_alumnos = []

for i in range(3):
  nombre_alumno = (input("Ingrese el nombre del alumno: ")).title()

  #ingreso de notas
  notas = []
  for j in range(3):
      nota = int(input("Ingrese una nota: "))
      notas.append(nota)
  tupla_notas = tuple(notas)

  #agregar nombre y tupla de notas al diccionario
  dic_alumno = {}
  dic_alumno['Nombre'] = nombre_alumno
  dic_alumno['Notas'] = tupla_notas

  #promedio
  acumulador = 0
  for h in notas:
    acumulador += h
  promedio = acumulador / len(notas)

  #guardar promedio en su diccionario
  dic_alumno['Promedio'] = promedio

  #guardar diccionario en la lista
  lista_alumnos.append(dic_alumno)


print(lista_alumnos)


"""

7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)
"""

aprobados_parcial1 = {"Agustín Pérez", "Juana Castro", "Valentina López", "Camila Gómez", "Sofía Romero", "Nicolás Medina", "Renata Rojas",
                      "Tomás Herrera", "Mía Vega", "Juan Cruz Morales"}
aprobados_parcial2 = {"Agustín Pérez", "Juana Castro", "Valentina López", "Lucía González", "Franco Molina", "Santiago Fernández",
                      "Emilia Navarro", "Julián Cabrera", "Isabella Sánchez", "Benjamín Ruiz"}

ambos_parciales = aprobados_parcial1 & aprobados_parcial2
print("Los que aprobaron ambos parciales son: ", ambos_parciales)

un_parcial_aprobado = aprobados_parcial1 ^ aprobados_parcial2
print("Los que aprobaron solo un parcial son: ", un_parcial_aprobado)

alumnos_universal = (aprobados_parcial1 | aprobados_parcial2)
print("Los que aprobaron al menos un parcial son: ", alumnos_universal)

"""8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
"""

dict_productos = {"Cartuchera": 10, "Lápiz": 5, "Cuaderno": 15, "Birome": 22}


while True:

  print(" ----------------")
  print(" ***** MENU *****")
  print("1. Consultar stock")
  print("2. Agregar unidades")
  print("3. Agregar producto")
  print("0. Salir")

  opcion = input("Ingrese una opción: ")

  match opcion:
    case "1":
      clave = (input("Ingrese el nombre del producto: ")).title()
      if clave in dict_productos:
        print(f"El stock de {clave} es {dict_productos[clave]}")
      else:
        print("El producto ingresado no se encuentra")

    case "2":
      clave = (input("Ingrese el nombre del producto: ")).title()
      cantidad = int(input("Ingrese la cantidad: "))
      dict_productos[clave] = dict_productos.get(clave, 0) + cantidad
      print(f"Se ha actualizado correctamente el stock de {clave}: {dict_productos[clave]} unidades")

    case "3":
      nuevo_prod = (input("Ingrese el nombre del producto: ")).title()
      cantidad = int(input("Ingrese la cantidad disponible: "))
      dict_productos[nuevo_prod] = cantidad
      print(f"Ha ingresado satisfactoriamente el producto {nuevo_prod}: {cantidad} unidades")

    case "0":
      break
    case _:
      print("Ingrese una opcion valida")

"""9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora.
"""

mi_agenda = {("lunes", "20:00"): "AySO", ("martes", "19:00"): "Matemáticas", ("miércoles", "20:00"): "Programación",
 ("jueves", "16:00"): "Programación", ("viernes", "17:00"): "Hora de consultas"}

while True:

  print(" ***** MI AGENDA *****")
  print("1. Consultar actividades")
  print("0. Salir")

  opcion = input("Ingrese la opcion deseada: ")

  match opcion:
    case "1":
        consulta_dia = (input("Ingresa el dia: ")).lower()
        consulta_hora = input("Ingresa la hora en formato hh:mm : ")

        for dia, hora in mi_agenda.keys():
            if dia == consulta_dia and hora == consulta_hora:
             print(f"Para el dia {dia} a las {hora} hay clases de: {mi_agenda[(dia,hora)]}")
             break
        else:
                print("No se encuentra ninguna clase en el horario indicado")

    case "0":
        break
    case _:
        print("Opcion incorrecta")

"""Permití consultar qué actividad hay en cierto día y hora.
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
"""

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción",
    "Perú": "Lima",
    "Colombia": "Bogotá",
    "México": "Ciudad de México",
    "España": "Madrid",
    "Italia": "Roma"
}

pc_invertido = {capital : pais for pais, capital in paises_capitales.items()}
print(pc_invertido)