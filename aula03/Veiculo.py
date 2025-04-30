from abc import ABC, abstractmethod

class Veiculo(ABC):  
    def __init__(self, modelo, ano = 2025):
        self.modelo = modelo
        self.ano = ano

    @abstractmethod  
    def exibir_detalhes(self):  
        pass

    def __str__(self):
        return self.modelo + "\nAno: " + str(self.ano)