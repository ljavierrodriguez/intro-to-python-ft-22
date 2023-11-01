# Condicionales

""" 

if condicion:
    sentencias
    
if condicion:
    sentencias
else:
    sentencias

if condicion:
    sentencias
elif condicion:
    sentencias
else:
    sentencias
    
and 
or
not

"""

a = 5
b = 10
c = 4


if a > b:
    print("Info")
    
if b == c:
    pass
else:
    pass

if a > b and a > c:
    print("A")
elif b > c:
    print("B")
else:
    print("C")
    
frutas = { "Pera", "Manzana", "Banana", "Uva"}
nombres = ["Hugo", "Paco", "Luis"]

if "Manzana" in frutas:
    print("Existe")
    
if "Hugo" in nombres:
    print("Hugo esta presente")
    
# ternario
mayor = "A" if a > b else "B"