"""Realizar un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>."""
# Crear diccionario vacio
datos = {}

# Pesdir y almacenar datos en el diccionario
nombre = input("Ingrese el nombre: ")
datos['nombre'] = nombre
edad = int(input(f"Ingrese la edad de {nombre}: "))
datos['edad'] = edad
direccion = input(f"Ingrese la direccion de {nombre}: ")
datos['direccion'] = direccion
telefono = int(input(f"Ingrese el telefono de {nombre}: "))
datos['telefono'] = telefono

# Imprimir datos del diccionario
print(f"{datos.get('nombre')} tiene {datos.get('edad')} años, vive en {datos.get('direccion')} y su numero de telefono es {datos.get('telefono')}")