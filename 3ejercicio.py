"""Realizarun programa que guarde en un diccionario los precios de repuestos de carro de la siguiente tabla, pregunte al usuario por un repuesto, 
la cantidad y muestre por pantalla el precio de ese número de repuestosde carro. Si elrepuesto no está en el diccionario debe mostrar un mensaje 
informando de ello.
Repuesto                Precio
Bujia                   1.40
Pastillas de freno      5.80
Radiador                300.50
Rodamiento              10.70"""

# Crear diccionario con los datos
repuestos = {'bujia' : 1.40, 'pastillas de freno' : 5.80, 'radiador' : 300.50, 'rodamiento' : 10.70}

# Crear variable para repetir el bucle
repetir = 'si'

while(repetir == 'si'):
    # Pedir nombre del repuesto
    repuesto = input('Ingrese el repuesto que desea: ').lower()
    # Condicional para saber si se encuentra el repuesto
    if(repuesto in repuestos):
        # Pedir la cantidad de repuestos
        cantidad = int(input(f'Ingrese de cantidad de {repuesto} que necesita: '))
        # Calcular el precio de la cantidad del repuesto
        precio = float(cantidad * repuestos.get(repuesto))
        # Imprimir el precio total
        print(f'El precio total para {cantidad} {repuesto} es de ${precio}')

    else:
        # Imprimir que no se encuentra el repuesto
        print(f'El repuesto {repuesto} no se encuentra disponible')

    # Preguntar si se desea cotizar una vez mas
    repetir = input('Desea cotizar otro repuesto? (si) (no): ').lower()
        
