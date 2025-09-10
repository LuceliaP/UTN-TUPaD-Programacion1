#1) Crear una lista con las notas de 10 estudiantes. Mostrar la lista completa.
#  Calcular y mostrar el promedio.Indicar la nota más alta y la más baja
'''
mis_notas = [8, 7, 9, 10, 5, 7, 6, 8, 8.5, 9.5]

# mostrar la lista completa
for i in range(len(mis_notas)):
    print(mis_notas[i])

#calcular y mostrar el promedio
acumulador = 0
for i in range(len(mis_notas)):
    acumulador += mis_notas[i]

promedio = acumulador / len(mis_notas)
print("El promedio de las notas es ", promedio)

# Indicar la nota mas alta y la mas baja

nota_mayor = 0
nota_menor = False

for i in range(len(mis_notas)):
    if mis_notas[i] > nota_mayor:
        nota_mayor = mis_notas[i]
    if nota_menor == False:
        nota_menor = mis_notas[i]
    elif mis_notas[i] < nota_menor:
        nota_menor = mis_notas[i]
    else:
        pass

print(f"La nota mas alta es {nota_mayor} y la nota mas baja es {nota_menor}")

# 2) Pedir al usuario que cargue 5 productos en una lista. Mostrar la lista ordenada alfabéticamente.
#  Investigue el uso del método sorted(). Preguntar al usuario qué producto desea eliminar 
# y actualizar la lista.

#Pedir al usuario que cargue 5 productos
mis_productos = []
for i in range(5):
    producto= input("Ingrese un producto ")
    mis_productos.append(producto)

print(mis_productos)

#Mostrar la lista ordenada alfabeticamente

mis_productos_orden = sorted(mis_productos)

for i in range(len(mis_productos_orden)):
    print(mis_productos_orden[i])

#Preguntar al usuario qué producto desea eliminar y actualizar la lista.

#Utilizo [:] para recorrer una copia, ya que si recorro la lista original, al eliminar un elemento en medio del recorrido,
#se genera un Index Error

no_deseable = input("Cual elemento desea eliminar? ")


for i in mis_productos[:]:
    if i == no_deseable:
        mis_productos.remove(i)

   
 # Muestro lista actualizada   
for i in mis_productos:
    print(i)


# 3) Generar una lista con 15 números enteros al azar entre 1 y 100. Crear una lista con los pares y otra con los impares.
#  Mostrar cuántos números tiene cada lista.

#Crear una lista con 15 numeros
import random
mi_lista = [random.randint(1,100) for i in range(15)]
print(mi_lista)

# Crear una lista con los pares y otra con los impares
lista_pares = []
lista_impares = []

for i in range(len(mi_lista)):
    if mi_lista[i] % 2 == 0:
        lista_pares.append(mi_lista[i])
    else:
        lista_impares.append(mi_lista[i])

print(lista_impares)
print(lista_pares)

#Mostrar cuantos numeros tiene cada lista
print(f"La lista de pares tiene {len(lista_pares)} numeros")
print(f"La lista de impares tiene {len(lista_impares)} numeros")


# 4) Dada una lista con valores repetidos: datos = [1,3,5,3,7,1,9,5,3], crear una nueva lista sin elementos repetidos. Mostrar el resultado

una_lista = [1,3,5,3,7,1,9,5,3]
una_lista_sindup = []

for i in una_lista:
    if i not in una_lista_sindup:
        una_lista_sindup.append(i)

print(una_lista_sindup)


# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase. Preguntar al usuario si quiere agregar un nuevo estudiante 
# o eliminar uno existente. Mostrar la lista final actualizada

lista_alumnos = ["Carla", "Nicolas", "Enrique", "Maricel", "Sofia", "Sergio", "Mateo", "Valeria"]

opciones = input("Quiere ingresar un nuevo estuiante? Ingrese 'S' para si y 'N' para no ")
if opciones == "S":
    nombre_nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    lista_alumnos.append(nombre_nuevo)
    print(f"El nombre {nombre_nuevo} ha sido agregado exitosamente")
    print("La lista actual de alumnos es: ", lista_alumnos)
elif opciones == "N":
    quiere_eliminar = input("Quiere eliminar un estudiante de la lista? Ingrese 'S' para si y 'N' para no ")
    if quiere_eliminar == "S":
        nombre_elim = input("Ingrese el nombre del alumno que quiere eliminar de la lista ")
        for i in lista_alumnos[:]:
            if i == nombre_elim:
                lista_alumnos.remove(i)
                print(f"El nombre {nombre_elim} ha sido eliminado exitosamente")
                print("La lista actual de alumnos es: ", lista_alumnos)
    elif quiere_eliminar == "N":
        print("Este es el fin del menu")
    else:
        print("Elija una opcion valida")
else: print("Elija una opcion valida")

print("Adios!")


# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).

lista_7 = [1, 2, 3, 4, 5, 6, 7]

ultimo = lista_7[-1] #<class 'int'>
resto = lista_7[:-1] #<class 'list'>
nueva_lista = [ultimo] + resto  #necesario el corchete para convertir ultimo a lista
print(nueva_lista) 



# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
#  Calcular el promedio de las mínimas y el de las máximas. Mostrar en qué día se registró la mayor amplitud térmica.

#Crear una matriz 
temp_semana = [
    [13, 21],
    [10, 21],
    [10, 22],
    [11, 18],
    [14, 19],
    [12, 19],
    [12, 20]
]

#Calcular el promedio de las minimas
cant_filas = len(temp_semana)

sumatoria = 0
for filamin in temp_semana:
    sumatoria += filamin[0]

promedio_min = sumatoria // cant_filas
print("El promedio de las temperaturas minimas fue de ", promedio_min)

#Calcular el promedio de las maximas

suma = 0
for filamax in temp_semana:
    suma += filamax[1]

promedio_max = suma // cant_filas
print("El promedio de las temperaturas maximas fue de ", promedio_max)

#Otro metodo construyendo listas con min y max
#minimas = [fila[0] for fila in temp_semana]
#maximas = [fila[1] for fila in temp_semana]
#promedio = sum(minimas)/len(minimas)

#Mostrar en qué día se registró la mayor amplitud térmica
contador = 0
mayor_dif = 0
bandera = False
for i in temp_semana:
    if bandera == False:
        mayor_dif = i[1] - i[0]
        bandera = True
    else:
        if i[1]-i[0] > mayor_dif:
            mayor_dif = i[1]-i[0]
    contador += 1

print(f"La mayor amplitud termina fue de {mayor_dif} y se encontro en el dia {contador}")

#Otra forma
#amplitudes = [fila[1]-fila[0] for fila in temp_semana]
#dia_mayor = amplitudes.index(max(amplitudes))+1


# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias. Mostrar el promedio de cada estudiante.
# Mostrar el promedio de cada materia.

matriz_notas = [

    [7, 8, 7],
    [10, 9, 7],
    [5, 4, 6],
    [10, 5, 7],
    [9, 8, 8]
]

#Mostrar el promedio de cada alumno
for fila in range(5):
    acumulador = 0
    for nota in range(3):
        acumulador += matriz_notas[fila][nota]
    promedio = acumulador / 3
    print(f"El promedio del alumno {fila+1} es de ", promedio)


#Mostrar el promedio de cada materia
for j in range(3):
    suma = 0
    for i in range(5):
        suma += matriz_notas[i][j]
    promedio_mat = suma / 5
    print(f"El promedio de la materia {j+1} es de {promedio_mat}")


#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). Inicializarlo con guiones "-" representando casillas vacías.
# Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# Mostrar el tablero después de cada jugada.

tablero = []

for i in range(3):
    fila = []
    for j in range(3):
        fila.append("-")
    tablero.append(fila)

for fila in tablero:
    for columna in fila:
        print(columna, end= " ")
    print()


jugador = "X"
jugadas = 0

while jugadas < 9:
    print(f"\nTurno del jugador {jugador}")


    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-2): "))

    if fila <0 or fila >2 or columna <0 or columna >2:
        print("Ingrese un numero valido")
        continue

    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        jugadas += 1
    else:
        print("Casilla ocupada, intente de nuevo")
        continue

    for fila in tablero:
        for columna in fila:
            print(columna, end= " ")
        print()

    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"

        '''

# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. Mostrar el total vendido por cada producto.
#  Mostrar el día con mayores ventas totales. Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [5, 7, 10, 2, 8, 7, 8],
    [8, 3, 4, 5, 8, 3, 2],
    [12, 1, 10, 1, 8, 7, 4],
    [6, 7, 9, 5, 8, 4, 2],
]

#Totales de cada producto
totales_prod = []

for i in range(4):
    total_producto = 0
    for j in range(7):
        total_producto += ventas[i][j]
    totales_prod.append(total_producto)
    print(f"Producto {i+1}: {total_producto}")

#Dia con mayores ventas

mayor_ventas = 0
dia_mayor = 0

for j in range(7):
    total_dia = 0
    for i in range(4):
        total_dia += ventas[i][j]
    print(f"Total de ventas del dia {j+1}: {total_dia}")
    if total_dia > mayor_ventas:
        mayor_ventas = total_dia
        dia_mayor = j

print(f"El dia con mayor ventas fue el {dia_mayor+1} con {mayor_ventas} productos vendidos")

#Indicar cual producto fue el mas vendido

mayor_producto = 0
indice_mayor = 0

for i in range(4):
    if totales_prod[i] > mayor_producto:
        mayor_producto = totales_prod[i]
        indice_mayor = i
print(f"El producto mas vendido fue el {indice_mayor+1}, con {mayor_producto} ventas")

