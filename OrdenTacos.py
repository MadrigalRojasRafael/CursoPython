from Tacos import *
from Bebidas import * 

#Creación de la Clase → OrdenTacos:
class OrdenTacos:
    #Variable de Clase para el Número de Orden:
    nOrden = 0

    def __init__(self, tacos, bebidas, nMesa):
        OrdenTacos.nOrden += 1
        self._nOrden = OrdenTacos.nOrden
        self._tacos = list(tacos)
        self._bebidas = list(bebidas)
        self._nMesa = nMesa

    #Método addTaco para agregar Tacos a la orden:
    def addTaco(self, taco):
        self._tacos.append(taco)

    #Método addBebida para agregar Bebidas a la orden:
    def addBebida(self, bebida):
        self._bebidas.append(bebida)

    #Metódo __str__() para visualizar los datos del Objeto:
    def __str__(self):
        totalTacos = float(len(self._tacos) * Tacos.precioTaco)
        totalBebidas = float(len(self._bebidas) * Bebidas.precioBebida)
        print(f" Orden 0{self._nOrden} ".center(60, "-"))
        print(f" Mesa 0{self._nMesa} ".center(60, "-"))
        tacos_str = ""
        for taco in self._tacos:
            tacos_str += taco.__str__() + "\n"
        print(f"Tacos:\n{tacos_str}")
        bebidas_str = ""
        for bebida in self._bebidas:
            bebidas_str += bebida.__str__() + "\n"
        print(f"Bebidas:\n{bebidas_str}")
        return f"Total: ${totalTacos + totalBebidas}"

