"""Realizarun programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
(por ejemplo, nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario."""
# Creamos el diccionario vacio
diccionario = {}

# Creamos variable para que el bucle se repita
repetir = 'si'
# Creamos variable para identificar las llaves del diccionario
iteracion = 1

# Creamos un bucle while para meter la cantidad de datos que queramos
while(repetir == 'si'):
    # Creamos una lista para almacenar los datos
    lista = []
    # Concatenamos la palabra Dato con la variable identificativa
    dato = 'Dato' + str(iteracion)

    # Pedimos el nombre
    nombre = input('Ingrese el nombre: ')
    # Almacenamos el nombre en la lista
    lista.append(nombre)
    edad = int(input(f'Ingrese la edad de {nombre}: '))
    lista.append(edad)
    sexo = input(f'Ingrese el sexo de {nombre}: ')
    lista.append(sexo)
    telefono = int(input(f'Ingrese el telefono de {nombre}: '))
    lista.append(telefono)
    correo_electronico = input(f"Ingrese el correo electronico de {nombre}: ")
    lista.append(correo_electronico)

    # Usamos como llave la variable dato concatenada con la variable iteracion y como llave la lista con los datos
    diccionario[dato] = lista

    # Creamos bucle para recorrer el diccionario e imprimirlo en pantalla
    for i in diccionario:
        print(diccionario)

    # Incrementamos en 1 la variable iteracion
    iteracion += 1

    # Pedimos opcion para repetir el bucle while
    repetir = input('Desea ingresar mas datos? (si) (no): ').lower()