'''
Realizar un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas 
se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el 
valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva 
factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el 
número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se 
preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el 
programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad 
pendiente de cobro.
'''

menu_facturas= "\nMENU \n\n"
menu_facturas+= "1. Registrar facturas\n"
menu_facturas+= "2. Consultar facturas\n"
menu_facturas+= "3. Pagar facturas\n"
menu_facturas+= "4. Salir\n"
menu_facturas+= "Opcion: "

diccionario_facturas = {}

codigo = 0

while(codigo!= 4):
    suma = 0
    codigo=int(input(menu_facturas))
    if(codigo == 1):
        solicita_ingreso = "si"

        while(solicita_ingreso == "si"):
            codigo = input("Ingrese el codigo de la factura: ").lower()
            precio = int(input(f"Ingrese el precio de la factura {nombre}: "))

            diccionario_facturas[codigo]=precio
            print()
            print(diccionario_facturas)
            solicita_ingreso = input("\nDesea ingresar otra factura? (si) (no): ").lower()
            print()
    elif(codigo == 2):
        print("\nRegistro total de facturas: ")
        for clave in diccionario_facturas:
            print(f"{clave} - {diccionario_facturas.get(clave)}")
    elif(codigo == 3):
        print("\nPagar facturas")
        codigo_fruta = input("Ingrese la factura que desea pagar: ").lower()
        if(codigo_facturas in diccionario_facturas):
            diccionario_facturas.pop(codigo_facturas)
            print("factura pagada")
        else:
            print(f"La factura ya se pago o no se encuentra {codigo_facturas} ")

print("Salio!")