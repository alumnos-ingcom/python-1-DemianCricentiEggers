################
# Nombre - @DemianCricentiEggers
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que a partir de tres variables de tipo entero
 retorne una tupla con dichos valores ordenados de menor a mayor. Y Viceversa
"""

# Reemplazar por las funciones a implementar del ejercicio

def ordenar_mayor_a_menor(uno, dos, tres):
    if uno > dos and uno > tres :
        if dos > tres :
            return (uno,dos,tres)
        else : 
            return (uno,tres,dos)
    if dos > tres and dos > uno :
        if uno > tres :
            return (dos,uno,tres)
        else :
            return (dos,tres,uno)
    if tres > uno and tres > dos :
        if uno > dos :
            return (tres,uno,dos)
        else:
            return (tres,dos,uno)

def ordenar_menor_a_mayor(uno, dos, tres):
    if uno > dos and uno > tres :
        if dos > tres :
            return (tres,dos,uno)
        else : 
            return (dos,tres,uno)
    if dos > tres and dos > uno :
        if uno > tres :
            return (tres,uno,dos)
        else :
            return (uno,tres,dos)
    if tres > uno and tres > dos :
        if uno > dos :
            return (dos,uno,tres)
        else:
            return (uno,dos,tres)