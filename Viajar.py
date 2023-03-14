class Viajes:
    pass

    def _init_(self, Destino):
        self.s = Destino

Destino1 = Viajes("EEUU")
Destino2 = Viajes("Francia")

class Alexandra(Viajes):
    pass

    def _init_(self, Nombre):
        self.Nombre = Nombre
    
    def Viajar(self):
        return'{} Viajar {}'.format(self.Nombre,Destino1)
    
Alexandra = Alexandra("Alexandra")

class Lorena(Viajes):
    pass

    def _init_(self, Nombre):
        self.Nombre = Nombre
    
    def Viajar(self):
        return'{} Viajar {}'.format(self.Nombre,Destino2)
    
Lorena = Lorena("Lorena")

print(Alexandra.Viajar())
print(Lorena.Viajar())