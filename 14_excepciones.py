### Manejo de excepciones ###
valueOne = 10
valueTwo = 0
valuethrew = "ABC"

# try:
#     result = valueOne /valueTwo
#     print("No se a producido un error")
# except:
#     Se ejecuta si se produce una expectión
#     print("Se a producido un error durante la división")

# try:
#     result = valueOne / int("3")
#     print("No se ha p`roducido un error")
# except:
#     print("Se ha producido un error durante la conversión o división")
# else: # Esto es opcional pero si sale bien se realiza esto tambíen
#     print("La ejecución se ha completa corretamente")
# finally: # Opcional pero si se pone siempre se va a ejecutar 
#     print("La ejecución del bloque try a terminado")

# try:
#     result= valueOne / int("valueTwo")
#     print("No se ha producido un error")
# except ZeroDivisionError:
#     print("Se ha un producido un ZeroDivision")
# except ValueError:
#     print("Se ha un producido un ValueError")
# except TypeError:
#     print("Se ha un producido un TypeError")

try:
    result= valueOne / int("valueTwo")
    print("No se ha producido un error")
except Exception as error_general:
    print(f"Se ha un producido un error inesperado:{error_general}")
