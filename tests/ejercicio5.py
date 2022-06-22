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

dividendo = int(input("Ingrese dividendo: "))
divisor = int(input("Ingrese divisor: "))

resultado , resto = division_lenta(dividendo, divisor)
print("EL RESULTADO DE LA DIVISION ES: ",resultado,"y su resto es",resto)
 
 
 
 