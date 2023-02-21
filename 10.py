'''
Realizar un programa que permita gestionar la base de datos de clientes de una empresa. Los 
clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor 
será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), 
donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe 
preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) 
Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En 
función de la opción elegida el programa tendrá que hacer lo siguiente:
• Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de 
datos.
• Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
• Preguntar por el NIF del cliente y mostrar sus datos.
• Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
• Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
• Terminar el programa.
'''

menu_clientes = "\nMENU \n\n"
menu_clientes += "1. Registrar cliente\n"
menu_clientes += "2. Eliminar cliente\n"
menu_clientes += "3. Mostrar todos los clientes\n"
menu_clientes += "4. Consultar clientes preferentes \n"
menu_clientes += "5. Salir\n"
menu_clientes += "Opcion: "

diccionario_clientes = {}

codigo = 0

while(codigo!= 5):
    suma = 0
    codigo=int(input(menu_clientes))

    if(codigo == 1):
        solicita_ingreso = "si"

        while(solicita_ingreso == "si"):
            nombre = input("Ingrese el nombre: ").lower()
            dirección = int(input(f"Ingrese la direccion {nombre}: "))
            telefono = int(input(f"Ingrese el telefono {nombre}: "))
            correo = int(input(f"Ingrese el correo {nombre}: "))
            preferente = int(input(f"Si es preferente marque 1 de lo contrario marque 0 {nombre}: "))
            diccionario_clientes[nombre]=direccion,telefono,correo,preferente
            print()
            print(diccionario_clientes)
            solicita_ingreso = input("\nDesea ingresar otro cliente? (si) (no): ").lower()
            print()
    elif(codigo == 2):
        print("\nEliminar cliente")
        nombre_clientes = input("Ingrese el cliente a que desea eliminar: ").lower()
        if(nombre_clientes in diccionario_clientes):
            diccionario_clientes.pop(nombre_clientes)
            print("Cliente eliminado")
        else:
            print(f"El cliente {nombre_clientes} no esta registrado")
    elif(codigo == 3):
        print("\nRegistro de clientes: ")
        for clave in diccionario_clientes:
            print(f"{clave} - {diccionario_clientes.get(clave)}")
    elif(codigo == 4):
        print("\nClientes preferenciales: ")
        if(diccionario_clientes[preferente]==1):
            for clave in diccionario_clientes:
                print(f"{clave} - {diccionario_clientes.get(clave)}")

print("Salio!")