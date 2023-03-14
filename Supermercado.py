class Supermercado:
    pass

    def _init_(self, Productos):
        self.s = Productos

Productos1 = Supermercado("Verduras")
Productos2 = Supermercado("Frutas")

class Alexandra(Supermercado):
    pass

    def _init_(self, Nombre):
        self.Nombre = Nombre
    
    def Vender(self):
        return'{} vender {}'.format(self.Nombre,Productos1)
    
Alexandra = Alexandra("Alexandra")

class Lorena(Supermercado):
    pass

    def _init_(self, Nombre):
        self.Nombre = Nombre
    
    def Vender(self):
        return'{} vender {}'.format(self.Nombre,Productos2)
    
Lorena = Lorena("Lorena")

print(Alexandra.Vender())
print(Lorena.Vender())