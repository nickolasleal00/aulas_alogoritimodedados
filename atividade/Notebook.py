from Produto import Produto

class Notebook(Produto):
    def __init__(self,modelo,cor,preco,categoria,tempo_de_bateria):
        super().__init__(modelo,cor,preco,categoria)
        self.__tempo_de_bateria = tempo_de_bateria 

    def getTempo_De_Bateria(self):
        return self.__tempo_de_bateria
    
    def setTempo_De_Bateria(self, valor):
        self.__tempo_de_bateria = valor

    def getInformacoes(self):
        return super().getInformacoes() + f"Tempo de bateria: {self.__tempo_de_bateria}Hrs" 
    
    def Cadastrar():
        print("Notebook cadastrado com sucesso!")
