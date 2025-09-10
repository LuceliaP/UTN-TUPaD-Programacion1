# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for x in range (0, 101,1):
    print (x)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

print ("Ingrese un numero entero: ")
num = input()

contador = 0
for x in num:
    contador += 1

print(f"El numero ingresado tiene {contador} digitos")


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

print ("Ingrese el valor de inicio")
val_inicio = int(input())
print("Ingrese el valor final")
val_fin = int(input())

sumatoria = 0

for x in range(val_inicio +1, val_fin, 1):
    sumatoria += x

print("La suma de los numeros comprendidos en el rango es ", sumatoria)


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

sumatoria = 0

num = int(input("Ingrese un numero "))

while num != 0:
    sumatoria += num
    num = int(input("Ingrese otro numero, ingrese cero para terminar "))

print("La suma de los numeros ingresados es", sumatoria)


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

num = int(input("Ingrese un numero: "))

num_secreto = 5
intento = 1

while num != num_secreto:
    num = int(input("Ingrese un numero: "))
    intento += 1

print("Adivinaste! El numero secreto es", num_secreto)
print(f"Lo has logrado luego de {intento} intentos")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range (100, 0, -2):
    print(i)



# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num_finali = int(input("Ingrese un numero entero positivo maximo a sumar "))

sumatoria = 0

for i in range(0, num_finali):
    sumatoria += i

print(f"La suma de los numeros comprendidos entre cero y {num_finali}, es de {sumatoria}")



# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos.

contador_par = 0
contador_impar = 0
contador_neg = 0
contador_pos = 0

for i in range(0, 100):
    num = int(input("Ingrese un numero "))
    if num % 2 == 0:
        contador_par += 1
    else:
        contador_impar +=1
    if num >= 0:
        contador_pos += 1
    else:
        contador_neg += 1

print(f"La cantidad de numeros pares ingresados son {contador_par}, la de impares es de {contador_impar}, la de numeros positivos es de {contador_pos} y la de negativos {contador_neg}")



# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores

contador_num = 0

for i in range (0,100):
    ingreso = int(input("Ingrese un numero "))
    contador_num += ingreso

print("La media de los valores ingresados es ", contador_num / 100)


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario.

numero = input("Ingrese el numero a invertir ")
num_invertido = ""

for i in range (len(numero) -1, -1, -1):
    num_invertido += numero[i]

print(f"Para el numero {numero}, su inversion es {num_invertido}")
