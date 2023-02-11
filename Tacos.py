#Creación de la Clase → Tacos:
class Tacos:
    #Variable de Clase para el Precio del Taco:
    precioTaco = float(30)

    #Variable de Clase para el Número del Taco:
    nTaco = 0

    #Método __init__() para inicializar los Objeto de la Clase → Tacos:
    def __init__(self, taco, cebolla, cilantro, salsaVerde, salsaRoja, limon):
        self._taco = str(taco)
        self._cebolla = str(cebolla)
        self._cilantro = str(cilantro)
        self._salsaVerde= str(salsaVerde)
        self._salsaRoja= str(salsaRoja)
        self._limon = str(limon)
        Tacos.nTaco += 1
        self._nTaco = Tacos.nTaco

    #Metódo __str__() para visualizar los datos del Objeto:
    def __str__(self):
        return f'''
    N° Taco: {self._nTaco}
        Taco: {self._taco}
        Cebolla: {self._cebolla}
        Cilantro: {self._cilantro}
        Salsa Verde: {self._salsaVerde}
        Salsa Roja: {self._salsaRoja}
        Limón: {self._limon}
    Precio: ${self.precioTaco}
        '''