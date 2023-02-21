"""Realizar un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} 
y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada 
una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso."""

# Creamos diccionario vacio
materias_creditos = {}
# Creamos variable suma para el total de creditos
suma = 0
# Creamos variable repetir para el bucle while
repetir = 'si'

# Creamos bucle while para meter la cantidad de datos que queramos
while(repetir == "si"):
    suma = 0
    # Pedimos los datos
    asignatura = input("Ingrese el nombre de la asignatura: ")
    creditos = int(input(f'Ingrese los creditos de la asignatura {asignatura}: '))
    # Llenamos el diccionario
    materias_creditos[asignatura] = creditos
    # Creamos bucle for para recorrer el diccionario e imprimirlo en pantalla, tambien para sumar los creditos
    for materia in materias_creditos:
        print(f'{materia} tiene {materias_creditos.get(materia)}')
        suma += materias_creditos.get(materia)
    # Preguntamos si desea ingresar mas datos
    repetir = input('Desea ingresar otra asignatura? (si) (no): ').lower()

# Imprimimos el total de creditos
print(f'El total de crditos del curso es {suma}')
