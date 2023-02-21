"""Realizarun programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla 
la misma fecha en
 formato dd de <mes> de aaaa donde <mes> es el nombre del mes."""
dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

fecha = {'dd': dia, 'mmm': mes, 'aaaa': año}
print(f"fecha: {fecha['dd']}-{fecha['mmm']}-{fecha['aaaa']}")