from abc import ABC,abstractmethod
from Categoria import Categoria

class Produto(ABC):
    def __init__(self,modelo,cor,preco,categoria):
        self.modelo = modelo
        self.cor = cor
        self._preco = preco
        self.categoria = categoria

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("Preço negativo não pode!")
        self._preco = valor    

    def getInformacoes(self):
        return (
            f"Modelo: {self.modelo}\n"
            f"Cor: {self.cor}\n"
            f"Preço: R$ {self.preco:.2f}\n"
            f"Categoria: {self.categoria}"
        )

    def __str__(self):
        return self.getInformacoes()
    
    @abstractmethod
    def Cadastrar():    
       pass