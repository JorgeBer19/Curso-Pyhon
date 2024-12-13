# my_condicion = 5 + 5 
# if my_condicion == 10:
#     print("se ejecuta la condición") 
#     var2 = 5+7
#     print("Imprimiendo la variable 2",var2)
# var1 = 6
#     print(var2)
#if ,elif, else

print("---------------------------")

my_condition= int(input("Dame un número , no letras:"))

if my_condition > 10 and my_condition <  20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual a 20")

print("Fin de programa")


my_string = ""
if not my_string:
    print("My cadena de texto está vacia")