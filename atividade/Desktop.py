from Produto import Produto


class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potencia_da_fonte):
        super().__init__(modelo,cor,preco,categoria)
        self._potencia_da_fonte = potencia_da_fonte
    
    def getPotencia_Da_Fonte(self):
        return self._potencia_da_fonte
    
    def setPotencia_Da_Fonte(self,valor):
        self._potencia_da_fonte = valor

    def getInformacoes(self):
        return super().getInformacoes() + f"Potência da fonte: {self._potencia_da_fonte}W"    

    def Cadastrar(self):
        print("Cadastrado com sucesso!")
               
  