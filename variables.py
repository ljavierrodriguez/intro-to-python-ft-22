# Variables 
""" 

Definir variables 

(no tiene palabras reservadas para ello)


Data Types


String
Int
Float
Boolean

None

Dict

Array: 
    List
    Tuple
    Set

func

"""


nombre = ""
apellido = ''
direccion = '''

asdasd
asdasdad
asdasd
asd

'''

nombre_completo = f"{nombre} {apellido}"

edad = 30 # int
precio = 10.50 # float

activo = True

open = False

postal_code = None
piso = None

persona = { # dict 
    "nombre": "John",
    "apellido": "Doe"
}

persona["apellido"]

# Array

# List
nombres = ["Hugo", "Paco", "Luis"]
nombres[1]

# Tuple
estatus = ("activo", "inactivo", "cancelado", "aprobado")
estatus[3]

# Set
frutas = { "Pera", "Manzana", "Uva", "Mandarina", "Banana"}


def sumar(a, b):
    return a + b