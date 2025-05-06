from PyQt5.QtWidgets import *
from Categoria import Categoria

class TelaCategoria(QMainWindow):
    def __init__(self, categorias):
        super().__init__()
        self.setWindowTitle("Categoria")
        self.setGeometry(200, 200, 300, 100)
        self.categorias = categorias

        self.layout = QVBoxLayout()
        self.lblNome = QLabel("Nome da categoria:")
        self.txtNome = QLineEdit()
        self.btnSalvar = QPushButton("Salvar")
        self.btnSalvar.clicked.connect(self.salvar)

        self.layout.addWidget(self.lblNome)
        self.layout.addWidget(self.txtNome)
        self.layout.addWidget(self.btnSalvar)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def salvar(self):
        nome = self.txtNome.text()
        if nome != "":
            categoria = Categoria(nome)
            self.categorias.append(categoria)
            QMessageBox.information(self, "Salvo", f"{categoria}")
            self.close()