#Es una coleccion ordenada de elementos 

### Listas ###

#Definición de listas
my_list= list() #Crear una lista vacia usando el constructor list()
my_other_list= [] #Imprime una lista vacia usando []

print(len(my_list))#Imprime la longitud de la lista, en este caso va a salir 0

print(len(my_other_list))#Imprime la longitud de la lista, en este caso va a salir 0

#Definir una lista con valores 

my_list =[35, 20, 40, 35,14]
print(my_list)

print(len(my_list))#Para ver la longitud

#Listas de tipos diferentes

my_type_list = ["Hola", 3, "Mundo", 56, 1.88, 3]

print(my_type_list)

print(len(my_type_list))#Para ver la longitud

#Acesso a elemntos de una lista

print(my_type_list[0])#Accede al primer elemento 
print(my_type_list[-1])#Accede al ultimo elemento 
print(my_type_list[-5])#Accede al primer elemento 
print(my_type_list.count(3))#Cuenta el número de elementos que se repite 
#Como buscar el indice termino Hola el my_type_list = ["Hola", 3,"Mundo", 1.88, 3]
my_type_list = ["Hola", 3, "Mundo", 56, 1.88, 3]
print(my_type_list.index("Mundo"))

#Desempaquetar una lista 
var1, var2,var3, var4, var5, var6 = my_type_list

print(var1, var2, var3)

caja, hola,var3, var4, var5, var6 = my_type_list
print(caja, hola, var3)

var1, var2 = my_type_list[0],my_type_list[5]
print(var1, var2)

#Concatenar dos listas Se concatena con un +
my_type_list1 = ["Hola", 3]

my_type_list2 = [ "Mundo", 56, 1.88, 3]

print(my_type_list1+my_type_list2)

list3 =my_type_list1 + my_type_list2

print(list3)

#CURL de elementos(Creción,Inserción,Actualización y Eliminación)

list3.append("Jorge")

print(list3)

list3.append("85")

print(list3)

list3.insert(3,"Jose")

print(list3)

list3.remove("Hola")

print(list3)

list3[0] = "Javier" #Actualiza el valor de una lista

print(list3)

resultado = list3.pop()#Borra  el último valor de la lista

print(list3)
print(resultado)

resultado = list3.pop(0)#Borra  el último valor de la lista

print(list3)
print(resultado)

del list3[1]
print(list3)

list4 = list3.copy()

print(list4)

list3.clear()

print(list3)
print(list4)

list4.reverse()

print(list4)
listtaint =[1, 2 ,444, 555]
listtaint.sort() # Ordena de menor a mayor 

print(listtaint)

listtaint.sort(reverse=True) #Pasarle una funcion a un parametro 

print(listtaint)

print(listtaint[1:3])

list_string = "Hola VAMOS A TOMAR POR ..."

print(list_string)
print(type(list_string))