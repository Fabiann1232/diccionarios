'''
Realizar un programa que cree un diccionario de traducción español-inglés. El usuario introducirá 
las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> 
separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. 
Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si 
una palabra no está en el diccionario debe dejarla sin traducir.
'''
diccionario =  {}
opcion =  'si'
while ( opcion ==  'si' ):
  espanol ,  ingles =  input ( "Ingrese la palabra en español y en ingles  " ) .split ()
  diccionario [ espanol ]  = ingles
  opcion =   input ( "Desea ingresar mas  palabras (si / no): " )
frase =  input ( "Ingrese la frase a traducir: " )
palabra = frase.split ( " " )
print ("Traduccion" )
for  i  in  palabra : 
    if  i  in  diccionario : print ( diccionario [ i ],  end= " " ) 
    else : print ( i ,  end= " " )