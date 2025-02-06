#Clase Libro
print("Hola Mundo")
class Book:
    def __init__(self, title, author):
        """
        Constructor de la clase Book.
        :param title: Título del Libro.
        :param author: Autor del Libro.
        """
        self.title = title #Propiedad pública: Titulo del libro
        self.author = author #Propiedad pública : autor del libro
        self.__is_borrowed = False #Propiedad privada: indica si el está prestado

    def borrow(self):
        """
        Metodo para prestar el libro,
        Retorna True si se prestó exitosamente, False si ya está prestado
        """
        if self.__is_borrowed:
            return False
        self.__is_borrowed = True
        return True

    def is_borrowed(self):
        """"
        Metodo para verificar si el libro está preparado
        """
        return self.__is_borrowed
    def return_book(self):
        """"
        Metodo para devolver el libro
        """
        self.__is_borrowed = False
    
    def __str__(self):
        """ 
        Representación en string del libro.
        """
        status = "Prestado" if my_book.is_borrowed() else "Disponible"
        return f"'{self.title} por {self.author} ({status})"

# Clase Biblioteca

class Library:
    def ___init__(self):
        """
        Constructor de la clase Library.
        Inicializa una lista vacía de libros
        """
        self.books = [] 

    def add_book(self, book):
        """
        Metodo para agragar un libri a la biblioteca.
        :param book: Instacia de la clase Book.
        """
        self.books.append(book)
        print(f"Libro '{book.title}' agragando a la biblioteca")

    def show_books(self):
        """
        Metodo para mostrar los libros disponibles en la bibliotecas.
        """
        if not self.books:
            print("La biblioteca está vacia.")
            return
        print("\nLibros en la biblioteca:")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book}")

    def borrow_book(self, title):
        """
        Metodo para prestar un libro.
        :param title: Título del libro a presentar.
        """
        for book in self.books:
            if book.title == title:
                if book.borrow():
                    print(f"Has presentado el libro: '{title}'.")
                return
            else:
                print(f"El libro '{title}' ya está predtado.")
                return
        print(f"No se encontró el libro con título:'{title}'.")

    def return_book():
        """
        Metodo para devolver un libro.
        :param title: Titulo del libro a devolver
        """
        for book in self.books:
            if book.title == title:
                book.return_book()
                print(f"Has devuelto el libro: '{title}'.")
                return
        print(f"No se encontró el libro con título:'{title}'.")

my_book = Book("Titulo 1", "Yo mismo")
# Ejecución  del proyecto 
if __name__ == "__main__":
    # Crear una instacia de la biblioteca
    my_library = Library()
    
    # Agregar libros a la biblioteca
    book1 = Book("Libro1","Autor 1")
    book2 = Book("Libro2","Autor 2")
    book3 = Book("Libro3","Autor 3")

    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    my_library.show_books()

    my_library.borrow_book("Libro2")




# # Prestar libro 
# my_book.borrow()
# print(my_book)

# # Devolver libro
# my_book.return_book()
# print(my_book)


# # Estado previo del libro
# status = "Prestado" if my_book.is_borrowed() else "Disponible"

# print(f"El libro está {status}")

# my_book.borrow()

# # Actualizar variable status
# print(f"El titulo es {my_book.title} y el autor es {my_book.author}")

# # Actualizar variable status  
# status = "Prestado" if my_book.is_borrowed() else "Disponible"
# print(f"El libro está {status}")

# my_book.return_book()

# # Actualizar variable status  
# status = "Prestado" if my_book.is_borrowed() else "Disponible"
# print(f"El libro está {status}")