class Persona:
    def __init__(self, nombre, apellidos, edad):
        self._nombre = nombre
        self._apellidos = apellidos
        self._edad = edad
    
    def __str__(self):
        return f"Nombre: {self._nombre} {self._apellidos}\nEdad: {self._edad} años"
    
    @property
    def Nombre(self):
        return self._nombre

    @property
    def Apellidos(self):
        return self._apellidos

    @property
    def Edad(self):
        return self._edad

    @Nombre.setter
    def Nombre(self, nombre):
        self._nombre = nombre

    @Apellidos.setter
    def Apellidos(self, apellidos):
        self._apellidos = apellidos

    @Edad.setter
    def Edad(self, edad):
        self._edad = edad

class Empleado (Persona):
    def __init__(self, nombre, apellidos, edad, puesto, sueldo):
        super().__init__(nombre, apellidos, edad)
        self._puesto = puesto
        self._sueldo = sueldo

    def __str__(self):
        return f"{super().__str__()}\nPuesto: {self._puesto}\nSueldo: {self._sueldo}"

    @property
    def Puesto(self):
        return self._puesto

    @property
    def Sueldo(self):
        return self._sueldo 

    @Puesto.setter
    def Puesto(self, puesto):
        self._puesto = puesto

    @Sueldo.setter
    def Sueldo(self, sueldo):
        self._sueldo = sueldo