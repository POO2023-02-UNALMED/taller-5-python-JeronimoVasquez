
from zooAnimales.animal import Animal
class Ave(Animal):

    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    @classmethod
    def cantidad(cls):
        return len(Ave._listado)
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        Ave.halcones +=1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        Ave.aguilas +=1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
    
    @classmethod
    def cantidadAves(cls):
        return Ave.halcones + Ave.aguilas

    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas