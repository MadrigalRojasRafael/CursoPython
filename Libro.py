# - Clase → Libro
class Libro: 
    #Variable de Clase para almacenar el ID de los Objetos:
    ID_libro = 0

    #Método __init__() para crear Objetos de la Clase Libro:
    def __init__(self, titulo, autor):
        Libro.ID_libro +=1
        self._ID_libro = Libro.ID_libro
        self._titulo = titulo
        self._autor = autor

    #Getter para la Variable de Instancia → titulo
    @property
    def titulo(self):
        return self._titulo

    #Getter para la Variable de Instancia → autor
    @property
    def autor(self):
        return self._autor

    #Getter para la Variable de Clase → ID_libro
    @property
    def ID_libro(self):
        return self._ID_libro

    #Setter para la Variable de Instancia → titulo
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    #Setter para la Variable de Instancia → autor
    @autor.setter
    def autor(self, autor):
        self._autor = autor

    #Método __str__() para visualizar la Información del Objeto:
    def __str__(self):
        return f'''
Título: {self._titulo}
Autor: {self._autor}
        '''