"""Realizarun programa que guarde en undiccionario el nombre de las 10 monedas más importantes y su equivalente en pesos colombianos, 
ej. {'Euro':4.444, 'Dollar':4.422, 'Yen':31.86, ...}, pregunte al usuario por una divisa y muestre su valor en pesos colombianosy 
realice la conversión de un valor ingresado por el usuario,emita un mensaje de aviso si la divisa no está en el diccionario."""

# Crear diccionario con los datos
tasas_de_cambio = {'Dolar neozelandes' : 3052, 'Yuan chino' : 713.27, 'Peso mexicano' : 266.44, 'Dolar canadiense' : 3631.11, 'Franco suizo' : 5292.70,
                   'Dolar australiano' : 3365.92, 'Libra esterlina' : 5889, 'Yen japones' : 36.45, 'Euro' : 5231, 'Dolar estadounidense' : 4899.45}

# Crear variable menu
menu = "\nTASAS DE CAMBIO\n\n"
menu += "1. Dolar neozelandes\n"
menu += "2. Yuan chino\n"
menu += "3. Peso mexicano\n"
menu += "4. Dolar canadiense\n"
menu += "5. Franco suizo\n"
menu += "6. Dolar australiano\n"
menu += "7. Libra esterlina\n"
menu += "8. Yen japones\n"
menu += "9. Euro\n"
menu += "10. Dolar estadounidense\n:"

# Variable para que el bucle funcione
repetir = 'si'
# Variable para la cantidad que se desea convertir en moneda extranjera
cantidad_convertir = 0
# Variable para almacenar la conversion
cantidad_convertida = 0

# Bucle para hacer conversiones de manera ilimitada
while(repetir == 'si'):
    # Variable para elegir una moneda e ingresar a un respectivo condicional
    opcion = int(input(menu))

    if(opcion == 1):
        cantidad_convertir = float(input('Ingrese la cantidad a convertir: '))
        cantidad_convertida = float(cantidad_convertir/tasas_de_cambio['Dolar neozelandes'])
        print(f"{cantidad_convertir} pesos colombianos son {cantidad_convertida} dolares neozelandeces")
    
    elif(opcion == 2):
        cantidad_convertir = float(input('Ingrese la cantidad a convertir: '))
        cantidad_convertida = float(cantidad_convertir/tasas_de_cambio['Yuan chino'])
        print(f"{cantidad_convertir} pesos colombianos son {cantidad_convertida} yuanes chinos")

    elif(opcion == 3):
        cantidad_convertir = float(input('Ingrese la cantidad a convertir: '))
        cantidad_convertida = float(cantidad_convertir/tasas_de_cambio['Peso mexicano'])
        print(f"{cantidad_convertir} pesos colombianos son {cantidad_convertida} pesos mexicanos")

    elif(opcion == 4):
        cantidad_convertir = float(input('Ingrese la cantidad a convertir: '))
        cantidad_convertida = float(cantidad_convertir/tasas_de_cambio['Dolar canadiense'])
        print(f"{cantidad_convertir} pesos colombianos son {cantidad_convertida} dolares canadienses")
    
    elif(opcion == 5):
        cantidad_convertir = float(input('Ingrese la cantidad a convertir: '))
        cantidad_convertida = float(cantidad_convertir/tasas_de_cambio['Franco suizo'])
        print(f"{cantidad_convertir} pesos colombianos son {cantidad_convertida} francos suizos")

    elif(opcion == 6):
        cantidad_convertir = float(input('Ingrese la cantidad a convertir: '))
        cantidad_convertida = float(cantidad_convertir/tasas_de_cambio['Dolar australiano'])
        print(f"{cantidad_convertir} pesos colombianos son {cantidad_convertida} dolares australianos")

    elif(opcion == 7):
        cantidad_convertir = float(input('Ingrese la cantidad a convertir: '))
        cantidad_convertida = float(cantidad_convertir/tasas_de_cambio['Libra esterlina'])
        print(f"{cantidad_convertir} pesos colombianos son {cantidad_convertida} libras esterlinas")

    elif(opcion == 8):
        cantidad_convertir = float(input('Ingrese la cantidad a convertir: '))
        cantidad_convertida = float(cantidad_convertir/tasas_de_cambio['Yen japones'])
        print(f"{cantidad_convertir} pesos colombianos son {cantidad_convertida} yenes japoneses")

    elif(opcion == 9):
        cantidad_convertir = float(input('Ingrese la cantidad a convertir: '))
        cantidad_convertida = float(cantidad_convertir/tasas_de_cambio['Euro'])
        print(f"{cantidad_convertir} pesos colombianos son {cantidad_convertida} euros")
    
    elif(opcion == 10):
        cantidad_convertir = float(input('Ingrese la cantidad a convertir: '))
        cantidad_convertida = float(cantidad_convertir/tasas_de_cambio['Dolar estadounidense'])
        print(f"{cantidad_convertir} pesos colombianos son {cantidad_convertida} dolares estadounidenses")
    
    else:
        print('|---LA DIVISA NO SE ENCUENTRA---|')
    
    repetir = input('Desea hacer otra conversion? (si) (no): ').lower()