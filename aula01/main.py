class Carro:

    def _init_(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        self.kilometragem =  0

    def incrementar(self, km):
        if km > 0:
            self.__kilometragem += km

    def setKM(self, km):
        if km > self.__kilometragem:
            self.__kilometragem = km

    def __str__(self):
        txt = "Modelo " + self.modelo
        txt += "\nAno " + str( self.ano )
        txt += "\nKilometragem " + str( self.__kilometragem )
        return txt

    def imprimir(self):
        print(self)

x = Carro("Doblo", 2025)
print( x )

