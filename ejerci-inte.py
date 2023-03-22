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
""" def get_int():
    number = ''
    while not type(number) is int:
        try:
            number = int(input("insert a number: "))
        except ValueError:
            number = int(input("insert a number: "))
    return number
get_int() """

# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
# siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
# datos.
#  mostrar(): Muestra los datos de la persona.
#  Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona():
    def __init__(self, nombre: str="", edad: int = 0, dni:int =0):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    @property
    def nombre(self):
        return self.__nombre
    @property
    def edad(self):
        return self.__edad
    @property
    def dni(self):
        return self.__dni
    
    @nombre.setter
    def nombre(self, nombre):
            self.__nombre = nombre

    @edad.setter
    def edad(self, edad):
        self.__edad = edad
        self.mayor_de_edad()
            
    @dni.setter
    def dni(self, dni):
        self.__dni = dni
        
    def mostrar(self):
        print(f'{self.nombre} edad: {self.edad} dni: {self.dni}')
        
    def mayor_de_edad(self):
        return self.__edad > 18
    
        
    
# 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
# persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
# opcional. Crear los siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
# directamente, sólo ingresando o retirando dinero.
#  mostrar(): Muestra los datos de la cuenta.
#  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
# negativa, no se hará nada.
#  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
# rojos.

class Cuenta():
    def __init__(self, titular, cantidad: float = 0.0):
        self.titular = titular
        self.__cantidad = cantidad
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    
    def mostrarCuenta(self):
        return print(f'Cuenta {self.__titular.mostrar()} | Cantidad: {self.__cantidad}')
        
    def ingresar(self, cantidad):
        if self.__cantidad > 0:
            self.__cantidad += cantidad
        
    def retirar(self, cantidad):
         if cantidad > 0:
            self.__cantidad -= cantidad
    
    
    
# 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
# CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
# además del titular y la cantidad se debe guardar una bonificación que estará expresada en
# tanto por ciento. Crear los siguientes métodos para la clase:
#  Un constructor.
#  Los setters y getters para el nuevo atributo.
#  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
# tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
# mayor de edad pero menor de 25 años y falso en caso contrario.
#  Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
#  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
# cuenta.


class CuentaJover(Cuenta):
    def __init__(self, titular: Persona, cantidad: float =0, bonificacion: float= 0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
        
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion=bonificacion
        
    def es_titular_valido(self):
        return self.titular.edad < 25 and self.titular.edad > 18
    
    def mostrar(self):
        print("Cuenta Joven", self.titular, self.cantidad)
        
    def retirar(self, cantidad: int):
        self.cantidad -= cantidad
        print(f'saldo actual {self.cantidad}')


lucas1 = Persona("Lucas R", 31, 123456)
cuenta = Cuenta( lucas1 , 100)
cuenta.mostrarCuenta()