### String ###

#Declaración de strings usando comillas simples y dobles.
#Se puede untilizar tanto comillas como comillas simples #
#Normalmente se les ponen un nombre que indique que hace dicha varible.
my_string = "Antonio" # Esta es con dobles comillas#
my_other_string =  'Riquelme'# Esta es con comillas simples#

print (my_string)

#Concatenar string con un espacio en blanco#
print (my_string + " " +  my_other_string)

#Crear un salto de linea#

variable3 = "Esto es un string\ncon salto de linea"

print(variable3)

#Insertar una tabulación#

variable4 = "\tEsto es un string con salto de linea"

print(variable4)

#Escapar caracteres especiales "Quieres ver los 
# caracteres especiales"

variable5 = "\\Esto es un string con salto de linea"

print(variable5)

#Formateo de string 

name, surname, age = "Jorge", "Bernal", 19

print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))

# Formateo antiguo usando %

print("Mi nombre es %s %s y mi edad es %d"% (name,surname,age))

# Concatenar varios string
print("Mi nombre es" + name +" "+ surname + "y mi edad es "+ str(age))


#Formateo usando f-string (moderno)

print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetando caracteres

languaje = "Ptyton"
a,b,c,d,r,f = languaje

print(a)
print(b)

#Dividir string (Slice)


languaje_slice = languaje[1:3] #Toma el segundo caracter hasta el 3 (Sin incluir este mismo)

print(languaje_slice) #output: yt

languaje_slice = languaje[1:] #Desde la posición 1 hasta el final

print(languaje_slice)

languaje_slice = languaje[-2] #Desde la posicion del final hacia atrás

print(languaje_slice)

languaje_slice = languaje[0:6:2] # Toma caracteres de indice 0 al 6 ....

print(languaje_slice)

#Revierte la cadena de texto
languaje_slice = languaje[::-1] 
print(languaje_slice)

###Funciones de string ###

#Reemplazar caracteres de un string 

fruit = "Strawberry"

fruit_remplace = fruit.replace('r','R' )
print(fruit_remplace)

#Convertir todo el texo a Mayúsculas

print(fruit.capitalize())# Convertir el primer caracter del texto.


#Convertir todo el texo a Mayúsculas

print(fruit.upper())# Pone todos los caracteres en mayúsculas

#Cuantos caracteres hay del mismo  tipo

print(fruit.count("r"))

#Contar todos los caracteres de una palabra
print(len(fruit))

print(f"la varible {fruit} tiene: " + str(len(fruit)))

numero_de_letras = len(fruit)
print(numero_de_letras)
print(str(numero_de_letras).isnumeric())

#Convertir todo el texto a Minúsculas

print(fruit.lower())# Pone todos los caracteres en minúsculas

#Verificar todo el texto a Minúsculas
print(fruit.islower())

#Verificar si comienza la cadenas con unos caracteres 
#Ejmplo Py
print(languaje.startswith("Py"))

