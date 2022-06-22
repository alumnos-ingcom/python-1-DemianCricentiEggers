################
# Nombre - @DemianCricentiEggers
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo

"""

# Reemplazar por las funciones a implementar del ejercicio

def compara(numero, otro_numero):
    if numero > otro_numero:
        retorno = -1
        return (retorno)
    if numero == otro_numero:
        retorno = 0
        return (retorno)
    if numero < otro_numero:
        retorno = 1
        return (retorno)


numero = int(input("ingrese un numero para iniciar la comparacion"))
otro_numero = int(input("ingrese otro numero para terminar la comparacion"))
retorno = compara(numero, otro_numero) 
if retorno == -1:
    print("el primer numero es mayor al segundo")
elif retorno == 0:
    print("ambos numeros son iguales")
elif retorno == 1:
    print("el segundo numero es mayor al primero")