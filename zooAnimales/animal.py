

class Animal():

    _totalanimales = 0
    
    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
    
    @classmethod  
    def totalPorTipo(cls):
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return f"""Mamiferos: {Mamifero.cantidadMamiferos()}\nAves: {Ave.cantidadAves()}\n
        Reptiles: {Reptil.cantidadReptiles()}\nPeces: {Pez.cantidadPeces()}\nAnfibios: {Anfibio.cantidadAnfibios()}"""
    
        
    def toString(self):
        if self.getZona() != None:
            return f"""Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}
            , habito en {self.getHabitat()} y mi genero es {self.getGenero()}, la zona en
            la que me ubico es {self.getZona()}, en el {self.getZona().getZoo()}"""
        
        else:

            return f"""Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi genero es {self.getGenero()}"""
    
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getEdad(self):
        return self._edad
    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat
    def setHabitat(self, habitat):
        self._habitat = habitat
    
    def getGenero(self):
        return self._genero
    def setGenero(self, genero):
        self._genero = genero
    
    def getZona(self):
        return self._zona
    def setZona(self, zona):
        self._zona = zona

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalanimales
    
    @classmethod
    def setTotalAnimales(cls, total):
        cls._totalanimales = total