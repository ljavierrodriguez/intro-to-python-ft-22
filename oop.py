# OOP (Object Oriented Programming)
'''
1. Clases y Objetos
2. Abstraccion
3. Encapsulamiento (public, protected, private)
4. Herencia
5. Polimorfismo

'''

class Persona:
    nombre = None
    apellido = None
    rut = None
    
    def __init__(self, nombre, apellido, rut):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
    
    def comer(self):
        pass
    
    def caminar(self):
        pass
    
    def saludar(self):
        return f"Hola, soy {self.nombre} {self.apellido}"
    
    
    
per1 = Persona("Pedro", "Perez", "1234556")
per2 = Persona("Miguel", "Cabrera", "12345678")
print(per1.saludar())
print(per2.saludar())

class Estudiante(Persona):
    grado = None
    facultad = None
    
    def __init__(self, nombre, apellido, rut, grado, facultad):
        super().__init__(nombre, apellido, rut)
        self.grado = grado
        self.facultad = facultad
        
    def saludar(self):
        return f"Hola, Soy el estudiante {self.nombre} {self.apellido} de la facultad de {self.facultad}"
    

est1 = Estudiante("John", "Doe", "123456", "1ro", "Ingenieria")
est2 = Estudiante("Jane", "Doe", "123458", "5to", "Odontologia")

print(est1.nombre)
print(est2.facultad)
