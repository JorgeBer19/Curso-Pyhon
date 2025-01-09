# Clase Vacía
class Animal:
    def __init__(self, especies, sonido, color="rojo", edad : int=0): 
        self.especies = especies # Propiedad pública
        self.__sonido = sonido # Propiedad privada
        self._color = color # Propiedad protegida
        self.edad = edad
    def make_sound(self):
        #Metodo publico que puede usarse por cualquier persona
        print(f"El {self.especies} hace {self.__sonido}")
    def get_sound(self):
        # Metodo que utiliza el objeto para acceder a la propiedad sonido
        return self.__sonido
    def grow_older(self):
        # Incrementa la edad en 1 año del objeto animal
        self.edad +=1
        if self.edad >15:
            print(f"El {self.especies} ya no hace Guau")
        else:
            print(f"El {self.especies} sigue vivo")
        print(f"El {self.especies} ahora tiene la edad de {self.edad}")


mi_animal_1 = Animal("Perro","Guau", "blue", 15)
mi_animal_2 = Animal("Gato","Miau")

print(type(mi_animal_1))
print(type(mi_animal_2))


# print(f"La especie es{mi_animal_1.especies} y tiene una edad de {mi_animal_1.edad}")
# print(f"La especie es{mi_animal_1._color} y tiene una edad de {mi_animal_1.edad}")
# print(mi_animal_2.edad)


#mi_animal_1.edad = 12

print(f"La especie es {mi_animal_1.especies} y tiene una edad de {mi_animal_1.edad}")

print(mi_animal_1.edad)

print(mi_animal_1.get_sound())


mi_animal_1.grow_older()
mi_animal_2.grow_older()