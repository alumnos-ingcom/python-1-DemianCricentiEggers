################
# Nombre - @DemianCricentiEggers
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se quiere transformar temperaturas en grados fahrenheit a grados 
centígrados y viceversa.

Escribir las funciones para convertir la temperatura en grados 
centigrados en fahrenheit como un número decimal, utilice esta 
formula para calcular los grados centígrados y retorne
el resultado obtenido. Y viceversa.
"""

# Reemplazar por las funciones a implementar del ejercicio

def convertir_a_fahrenheit(centigrados):
    fahrenheit = (centigrados * 9/5) + 32
    return (fahrenheit)
def convertir_a_centigrados(fahrenheit):
    centigrados = (fahrenheit - 32) * 5/9
    return (centigrados)