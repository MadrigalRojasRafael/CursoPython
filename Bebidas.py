#Creación de la Clase → Bebidas: 
class Bebidas:
    #Variable de Clase para el Precio de Bebida:
    precioBebida = float(25)

    #Variable de Clase para el Número de la Bebida:
    nBebida = 0

    #Método __init__() para inicializar los Objeto de la Clase → Bebidas:
    def __init__(self, bebida):
        self._bebida = str(bebida)
        Bebidas.nBebida += 1
        self._nBebida = Bebidas.nBebida

    def __str__(self):
        return f'''
    N° Bebida: {self._nBebida}
        Bebida: {self._bebida}
    Precio: ${self.precioBebida}
    '''
