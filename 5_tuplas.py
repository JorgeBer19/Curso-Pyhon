#TUPLA
#Dos formas de declarar una tupla
my_tupla = tuple() #1

my_other_tupla = () #

my_tuple = ()
my_tuple =  "hola"
var1 = (34,45,45)

var2 = (34,45,45,"hola","mundo")

print(var1)

print(var2)

print(my_tuple)

print()
# Accesos a información de la tupla
print(var1[0]) # Acceso al primer valor
print(var1[-1]) # Acceso al último valor de la tupla

# Error fuera de rango
#print(var1[4]) # Acceso al cuarto valorm
#print(var1[-6]) # Acceso al sexto valor

#contra k c Comenta
# contro k u Descomenta

#Concatnación de tuplas

var3 = ("Hola", "Jose")

var4 = (":", "Dime tu edad")

var5 = var3 + var4

print(var5)

#Dividir  tuplas 

var6 = var5[0:2]

print(var6)

# Ver indices de contenido de una tupla

print(var5.index("Hola"))

print(var5.index("Jose"))

#Conta veces que se repite un valor en una tupla 


print(var5.count("Hola"))

var5 = list (var5)

print(tuple(var5))

print(var5)
var5.append("23")

var5 = tuple(var5)
print(type(var5))
print(var5)

