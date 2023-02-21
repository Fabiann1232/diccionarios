'''
Realizar un programa que cree un diccionario simulando una cesta de la compra. El programa debe 
preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida 
terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el 
siguiente formato
Lista de la compra
Artículo 1 Precio
Artículo 2 Precio
Artículo 3 Precio
… …
Total Coste
'''
menu_cesta= "\nMENU \n\n"
menu_cesta+= "1. Registrar articulo\n"
menu_cesta+= "2. Consultar registro completo de inventario de cesta y precio\n"
menu_cesta+= "3. Salir\n"
menu_cesta+= "Opcion: "


diccionario_cesta={}

codigo=0

while(codigo!=3):
    suma =0
    codigo=int(input(menu_cesta))

    if(codigo == 1):
        solicita_ingreso = "si"

        while(solicita_ingreso == "si"):
            nombre = input("Ingrese el articulo: ").lower()
            precio = int(input(f"Ingrese el precio {nombre}: "))

            diccionario_cesta[nombre]=precio
            print()
            print(diccionario_cesta)
            solicita_ingreso = input("\nDesea ingresar otro articulo? (si) (no): ").lower()
            print()
    elif(codigo == 2):
        print("\nRegistro total de articulos y precio: ")
        for clave in diccionario_cesta:
            print(f"{clave} - {diccionario_cesta.get(clave)}")
            
print("Salio!")