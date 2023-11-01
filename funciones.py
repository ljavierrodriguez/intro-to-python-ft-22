# Funciones
""" 

def nombre_funcion(params, ....):
    sentencias
    

nombre_funcion = lambda params,... : sentencia 



"""
# parametros posicionales
def sumar(a, b):
    return a + b
sumar(10, 10)

# paramatro con valor por defecto
restar = lambda a, b = 10: a - b
restar(10)

# paramtros Keywords
def nombre_completo(nombre = "Anonimous", apellido = ""):
    return f"{nombre} {apellido}"

nombre_completo() # Anonimous
nombre_completo(apellido="Doe", nombre="John") # John Doe
nombre_completo("Jane", "Doe")

# Empaquetamiento de argumentos 
def suma(*args):
    resultado = sum(args)
    return resultado

resultado = suma(1, 2, 3, 4, 5)

# Agrupacion de argumentos keywords
""" 
kargs = {
    "nombre": "",
    "apellido": ""
} 
"""
def empleado(**kargs):
    return f"{kargs['nombre']} {kargs['apellido']}"

empleado(nombre="Luis", apellido="Rodriguez")
empleado(nombre="Jane", apellido="Doe")