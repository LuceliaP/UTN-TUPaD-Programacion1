
"""

1. Crear archivo inicial con productos: Crear un archivo de texto llamado
productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
"""

#crear un archivo
with open("productos.txt", "w") as archivo:
  archivo.write("nombre,precio,cantidad\n")

#chequeo cómo se guardó
with open("productos.txt", "r") as archivo:
  contenido = archivo.read()
  print(contenido)

"""2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30
"""

# creo una lista de ingresos

ingresos = [
    "lapicera,120.5,30\n",
    "cartuchera,524,10\n",
    "mochila,110000,5\n"
]
#voy a utilizar el modo "w" porque quiero sobreecribir el contenido del codigo anterior
with open("productos.txt", "w") as archivo:
  archivo.writelines(ingresos)

#printeo el contenido para chequar la carga de la lista
with open("productos.txt", "r") as archivo:
  contenido = archivo.read()
  print(contenido)

#formateo de la lectura del archivo

def mostrar_productos():
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            print(f"Producto: {nombre.capitalize()} | Precio: ${precio} | Cantidad: {cantidad}")

"""3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente.
"""
mostrar_productos()

def agregar_producto():
    opcion = input("Desea ingresar un nuevo producto? Escriba S por sí y N por no: ")
    if opcion == "S" or opcion == "s":

        nuevo_nombre = input("Ingrese el nombre del producto: ")

        nuevo_precio = input("Ingrese el precio: ")

        while not nuevo_precio.isdigit():
                print("Por favor ingrese solamente numeros")
                nuevo_precio = input("Ingrese el precio: ")

        nuevo_precio = int(nuevo_precio)

        nuevo_cantidad = input("Ingrese la cantidad: ")

        while not nuevo_cantidad.isdigit():
            print("Por favor ingrese solamente numeros")
            nuevo_cantidad= input("Ingrese la cantidad: ")

        nuevo_cantidad = int(nuevo_cantidad)

        with open("productos.txt", "a") as archivo:
            archivo.write(f"{nuevo_nombre},{nuevo_precio},{nuevo_cantidad}\n")
        print("Producto agregado con éxito")
    else:
        print("Gracias por visitar el catálogo")

#Se vuelve a mostrar la lista de productos actualizados
mostrar_productos()

"""4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad
"""

#crear una lista y un archivo para cargarle la lista
lista = [
    "harina,2000,10\n",
    "maicena,2200,8\n",
    "arroz,1800,2\n"
]
with open("mi_archivo.txt", "w") as archivo:
  archivo.writelines(lista)

def cargar_lista_de_diccionarios():
  productos = []
  with open("mi_archivo.txt", "r") as archivo:
    for linea in archivo:
      nombre, precio, cantidad = linea.strip().split(",")
      producto = {
         "Nombre": nombre.capitalize(),
         "Precio": float(precio),
         "Cantidad": int(cantidad)
      }
      productos.append(producto)
  return productos


"""5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error.
"""

def buscar_producto(productos):
    prod_buscado = input("Ingrese un producto para buscar: ").capitalize()
    bandera = False
    for producto in productos:
       if producto["Nombre"].lower() == prod_buscado.lower():
            print(f"Producto encontrado: {producto['Nombre']} | Precio: ${producto['Precio']} | Cantidad: {producto['Cantidad']}")
            bandera = True
            break
    if not bandera:
        print("Producto no encontrado.")

"""6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista.

"""

actualizacion = [
    "lapicera,13000,15\n",
    "cartuchera,55000,10\n",
    "mochila,130000,4\n"
]

def guardar_productos_actualizados(productos_gpa):
   with open("productos.txt", "w") as archivo:
        archivo.writelines(actualizacion)
        print("Archivo actualizado correctamente.")

guardar_productos_actualizados(actualizacion)
#chequeo el guardado
mostrar_productos()