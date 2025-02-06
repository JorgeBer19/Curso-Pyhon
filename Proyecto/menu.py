from library import Library  # Importamos la clase Library
from book import Book  # Importamos la clase Book

def añadir (title ,author)
    resultado= numero1 + numero2
    return resultado

class Menu:
    def __init__(self):
        """
        Constructor de la clase Menu.
        """
        #Propiedad llamada Libreria 
        self.library = Library()
    def mostrar_menu(self):
        print("-----------------------------------")
        print("-----------------------------------")
        print("-------------Biblioteca------------")
        print("----------------Menú---------------")
        print("-----------------------------------")
        print("Elige la operación que desea realizar")
        print("(1) Añadir")
        print("(2) Reservar")
        print("(3) Devolver")
        print("(4) Lista libros")
        print("(5) Salir")
        operacion= int(input("Número: "))
        return operacion

# while True:
#     operacion = mostrar_menu()
#     if operacion == 1:
#         print("Añadir")
#         Nombre = str(input("Inserte Nombre del Libro"))
#         Autor = str(input("Inserte Nombre del Autor"))
#         print("La suma es: ")
#         print(suma(numero1,numero2 ))
#         input("Pulsa para seguir")

#     if operacion == 2:
#         print("Resta")
#         numero1 = int(input("Primer número"))
#         numero2 = int(input("Segundo número"))
#         print("La resta es: ")
#         print(resta(numero1,numero2 ))
#         input("Pulsa para seguir")

#     if operacion == 3:
#         print("Multiplicación")
#         numero1 = int(input("Primer número"))
#         numero2 = int(input("Segundo número"))
#         print("La multiplicación es: ")
#         print(multiplicación(numero1,numero2 ))
#         input("Pulsa para seguir")

#     operacion = mostrar_menu()
#     if operacion == 4:
#         print("División")
#         numero1 = int(input("Primer número"))
#         numero2 = int(input("Segundo número"))
#         print("La Divisiónn es: ")
#         print(division(numero1,numero2 ))
#         input("Pulsa para seguir")
        
#     operacion = mostrar_menu()
#     if operacion == 5:
#         print("Adíos")
#         break