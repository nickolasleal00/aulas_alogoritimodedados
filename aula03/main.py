import sys
from PyQt5.QtWidgets import QApplication

from TelaVeiculo import TelaVeiculo
from TelaCarro import TelaCarro
from TelaCategoria import TelaCategoria

app = QApplication(sys.argv)

#telaVeiculo = TelaVeiculo("Cadastro de Veículo")
#telaVeiculo.show()

categorias = []

telaCate = TelaCategoria("Selecione a Categoria", categorias)
telaCate.show()

telaCarro = TelaCarro("Cadastro de Carro", categorias, telaCate)
telaCarro.show()

#telaCate.telaCarro = telaCarro

sys.exit(app.exec_())