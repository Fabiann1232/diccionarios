'''
El directorio de los clientes de una empresa está organizado en una cadena de texto como la de 
más abajo, donde cada línea contiene la información del nombre, email, teléfono, cedula, y el 
descuento que se le aplica. Las líneas se separan con el carácter de cambio de línea \n y la primera 
línea contiene los nombres de los campos con la información contenida en el directorio.
cedula;nombre;email;teléfono;descuento\1001234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n
Realizar un programa que genere un diccionario con la información del directorio, donde cada 
elemento corresponda a un cliente y tenga por clave su cedula y por valor otro diccionario con el
resto de la información del cliente. Los diccionarios con la información de cada cliente tendrán 
como claves los nombres de los campos y como valores la información de cada cliente 
correspondientes a los campos.
'''
cadena =  'cedula;nombre;email;teléfono;descuento/1001234567;Luis  González;luisgonzalez@mail.com;656343576;12.5\n'

linea = cadena.split ( '\n' )
informacion = linea [ 0 ] .split ( '/' )
clave = informacion [ 0 ] .split ( ';' )
valor = informacion [ 1 ] .split ( ';' )

datos =  {}
for  i  in range ( 1 , len ( clave )):
  datos [ clave [ i ]]  = valor [ i ]

directorio =  {}
llave = valor [ 0 ]
directorio [ llave ]  = datos
print ( directorio )