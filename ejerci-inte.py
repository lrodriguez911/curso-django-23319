# Ejercicios integradores para revisar en la clase 7
# 1. Escribir una función que calcule el máximo común divisor entre dos números.
""" def mcd(a, b):
    result = 0
    if b == 0:
        result = a
    else:
        result = mcd(b, a % b)

    return result

mcd(90, 50) """
    
# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números
""" def mcm(a,b):
    result = (a * b )// mcd(a,b)
    return result

mcm(50, 20) """

# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

""" def strToDict(str):
    str = input() or "la casa esta en la colina"
    palabras = str.split()
    
    dict = {}
    
    for palabra in palabras:
        if palabra in dict:
            dict[palabra] += 1
        else:
            dict[palabra] = 1
    return dict
strToDict("la casa esta en la colina") """

# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia.

""" def dictToTup(dict):
    dictOrd = sorted(dict.items(), key=lambda x:x[1])
    return dictOrd[-1]
    
dictToTup(strToDict("la casa esta en la colina")) """
# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
# ejercicio tanto de manera iterativa como recursiva. 


""" def get_int():
    try:
        int = int(input("insert a number: "))
    except ValueError:
        get_int()
    return int """
def get_int():
    number = ''
    while not type(number) is int:
        try:
            number = input("insert a number: ")
        except ValueError:
            print("SOlo numeros")
    return number
get_int()