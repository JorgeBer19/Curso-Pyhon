#Variables
pi = 3.14

###Funciones que no devuelven nada ###

def imprimir_hola_mundo():
    print("Hola Mundo")

#imprimir_hola_mundo()

def suma (var1,var2):
    print(var1 + var2)
#suma(2,5)

def sumar():
    var1 = int(input("Dame el primer número: "))
    var2 = int(input("Dame el segundo número: "))
    suma (var1,var2)
#sumar()

def multiplicar_por_pi_por_un_valor_dado(valor:int):
    print(valor*pi)

#multiplicar_por_pi_por_un_valor_dado(34)

def resta(var1,var2):
    resultado = var1 - var2
    return resultado # Esta devuelve algo 
var3 = resta(4,2)
print(var3)

def encriptar(texto):   
    # hacer encriptación 
    return texto


