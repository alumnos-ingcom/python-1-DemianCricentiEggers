################
# Nombre - @DemianCricentiEggers
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que haga la suma entre dos números enteros
sin hacer la operación de manera directa. Esto quiere decir que 
para hacer la suma entre 4 y 3, las operaciones resultantes
deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero 
positivo y negativo.

"""

# Reemplazar por las funciones a implementar del ejercicio

def suma_lenta(numero, otro_numero):
    resultado = otro_numero 
    if numero < 0:
        while numero != 0 :
            resultado = resultado - 1
            numero = numero + 1
        return (resultado)
    elif numero > 0:
        while numero != 0 :
            resultado = resultado + 1
            numero = numero - 1
        return (resultado)
    else:
        return (resultado)