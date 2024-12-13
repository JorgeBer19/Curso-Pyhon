# Imprimir por pantalla 
# Seleccionar una de las siguintes operaciones:
    #Suma 
    #Resta
    #Multiplicación
    #División
#El programa pedítra dos números por pantalla
# y mostrará el resultado final de la operación

def suma (numero1,numero2):
    resultado= numero1 + numero2
    return resultado
def resta (numero1,numero2):
    resultado = numero1 - numero2
    return resultado

def division (numero1,numero2):
    resultado= numero1 / numero2
    return resultado

def multiplicación (numero1,numero2):
    resultado = numero1 * numero2
    return resultado

def mostrar_menu():
    print("-----------------------------------")
    print("-----------------------------------")
    print("------------Calculadora------------")
    print("-----------------------------------")
    print("-----------------------------------")
    print("Elige la operación que desea realizar")
    print("(1) Suma")
    print("(2) Resta")
    print("(3) Multiplicación")
    print("(4) División")
    print("(5) Salir")
    operacion= int(input("Número: "))
    return operacion

while True:
    operacion = mostrar_menu()
    if operacion == 1:
        print("Suma")
        numero1 = int(input("Primer número"))
        numero2 = int(input("Segundo número"))
        print("La suma es: ")
        print(suma(numero1,numero2 ))
        input("Pulsa para seguir")

    if operacion == 2:
        print("Resta")
        numero1 = int(input("Primer número"))
        numero2 = int(input("Segundo número"))
        print("La resta es: ")
        print(resta(numero1,numero2 ))
        input("Pulsa para seguir")

    if operacion == 3:
        print("Multiplicación")
        numero1 = int(input("Primer número"))
        numero2 = int(input("Segundo número"))
        print("La multiplicación es: ")
        print(multiplicación(numero1,numero2 ))
        input("Pulsa para seguir")

    operacion = mostrar_menu()
    if operacion == 4:
        print("División")
        numero1 = int(input("Primer número"))
        numero2 = int(input("Segundo número"))
        print("La Divisiónn es: ")
        print(division(numero1,numero2 ))
        input("Pulsa para seguir")
        
    operacion = mostrar_menu()
    if operacion == 5:
        print("Adíos")
        break