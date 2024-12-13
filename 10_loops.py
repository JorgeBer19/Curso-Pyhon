### LOOPS ###
# While
my_condition = 0

#while True:
#    print(my_condition)
#    my_condition += 12
#else: # es opcional
#   print("Mi condicion es mayor o igual a 10 ")


while my_condition <20:
    my_condition+=1
    if my_condition ==15:
        print("Se a detiene la ejecución")
        break
    print(my_condition)
print("Fin de programa")

### Tablas de multiplicar
my_condition = 0
numero= int(input("Dame un número , no letras:"))
while my_condition <10:
    my_condition +=1
    if my_condition ==11:
        print("Se detiene la ejecución")
        break
    resultado = my_condition * numero
    print(f" {my_condition} x {numero} = {resultado}")
print("Fin de programa")
