#CLASE PRODUCTOS:
# + Contador de productos → Variable de Clase
# - ID producto → int
# - Nombre producto → str
# - Precio → float
# Método __str__()

#Creamos la clase → Productos:
class Productos:

    #Variable de clase para el Contador de Productos → productos_agregados:
    productos_agregados = 0

    #Método __init__() para poder crear los Objetos:
    def __init__(self, nombre, precio):
        Productos.productos_agregados += 1
        self._id_producto = Productos.productos_agregados
        self._nombre = str(nombre)
        self._precio = float(precio)

    #Método getter para el atributo → id_producto:
    @property
    def id_producto(self):
        return self._id_producto

    #Método getter para el atributo → nombre:
    @property
    def nombre(self):
        return self._nombre

    #Método getter para el atributo → precio:
    @property
    def precio(self):
        return self._precio

    #Método setter para el atributo → nombre:
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    #Método getter para el atributo → precio:
    @precio.setter
    def precio(self, precio):
        self._precio = precio

    #Método __str__() para visualizar la información del Objeto:
    def __str__(self):
        return f"ID: 0{self.id_producto}\nNombre: {self.nombre}\nPrecio: {self.precio}"