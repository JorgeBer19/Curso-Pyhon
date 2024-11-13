#Sets : Es un conjunto , es decir una colección de elementos únicos y desordenados
#Dos tipos de 
my_set = set()

my_other_set = {}

print(type(my_set))
print(type(my_other_set)) 

var1 = {"Hola","Jose", 34}

print(var1)
print(type(var1))

var1.add ("Que tal")

print(var1)

var1.add("Hola") 

print(var1)

#var1.add("Hola","Hola") # No se pueden añadir más de uno a la vez 

#Eliminar

var1.remove("Hola")

print(var1)

#No elimita todo Da un error
    #var1.remove()

    #print(var1)

#Busqueda de elemento en el set(conjunto)

print("Jose" in var1)

#Transformación

var3 = list(var1)

print(var3)

var3 = tuple(var1)

print(var3)

#Union 

my_other_set = {"Kotin", "Swift", "Python"}

my_other_languages ={"php", "Css"}

var_union = my_other_set.union(my_other_languages).union(["JavaScript", "C#"])

print(var_union)


#var_union = my_other_set.union(my_other_set_languages)
 #Diferences

my_other_set_languages = {"JavaScript", "C#"}

print(var_union.difference(my_other_set_languages))

