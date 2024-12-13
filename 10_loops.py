### LOOPS ###
# While
my_condition = 0

#while True:
#    print(my_condition)
#    my_condition += 12
#else: # es opcional
#   print("Mi condicion es mayor o igual a 10 ")


# while my_condition <20:
#     my_condition+=1
#     if my_condition ==15:
#         print("Se a detiene la ejecución")
#         break
#     print(my_condition)
# print("Fin de programa")

# ### Tablas de multiplicar
# my_condition = 0
# numero= int(input("Dame un número , no letras:"))
# while my_condition <10:
#     my_condition +=1
#     if my_condition ==11:
#         print("Se detiene la ejecución")
#         break
#     resultado = my_condition * numero
#     print(f" {my_condition} x {numero} = {resultado}")
# print("Fin de programa")

# For 

my_list = [12, 34, 45, 67, 80, 23, 6]
for numero in my_list:
    print(numero)

my_tupla = ("Hola", 34, 45, 67, 80, 23, 6)
for item in my_tupla:
    item = item * 8
    print(item)
print("---------------------------")
my_set = {"Hola", 34, 45, 67, 80, 23, 6}
for item in my_set:
    item = item * 8
    print(item)

print("---------------------------")
my_dict = {"Nombre":"Pepe", 34: "Hola"}
for item in my_dict:
    print(my_dict[item])

    print("---------------------------")
my_dict = {"Nombre":"Pepe", 34: "Hola"}
for item in my_dict:
    print(f"Dentro de item hay; {item}")
    print(f"El valor para la clave {item}) es  {my_dict[item]}")

for item in my_dict:
    if item == "Nombre":
        print("Encontrado la clave nombre")