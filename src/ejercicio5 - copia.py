################
# Nombre - @DemianCricentiEggers
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que mediante restas sucesivas, obtenga 
el valor del cociente y resto de dos números enteros.

"""

# Reemplazar por las funciones a implementar del ejercicio

def division_lenta(dividendo, divisor):
    resultado = 0
    div = dividendo
    while divisor <= dividendo  :
        resultado = resultado + 1
        dividendo = dividendo - divisor
    resto = div - (resultado * divisor)
    return (resultado,resto)