# - Clase → Biblioteca
import os

class Biblioteca:

    #Variable de Clase para almacenar los datos de los Libros:
    catalogoLibros = "catalogoLibros.txt"

    #Método de Clase para poder agregar elementos al documento:
    @classmethod
    def addLibro(cls, libro):
        with open(Biblioteca.catalogoLibros, "a", encoding="utf8") as catalogo:
            catalogo.write(f"ID: {libro.ID_libro}\nTítulo: {libro.titulo}\nAutor: {libro.autor}\n")

    #Método de Clase para poder visualizar los elementos del documento:
    @classmethod
    def removeLibros(cls):
        os.remove(cls.catalogoLibros)
        print(" No hay libros disponibles por el momento ".center(60, "-"))

    #Método de Clase para poder visualizar los elementos del documento:
    @classmethod
    def listLibros(cls):
        with open(Biblioteca.catalogoLibros, "r", encoding="utf8") as catalogo:
            print(" Libros disponibles ".center(60, "-"))
            print(catalogo.read())