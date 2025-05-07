from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QVBoxLayout, QPushButton, QWidget

class TelaDesktop(QMainWindow):
    def __init__(self, categorias):
        super().__init__()
        self.categorias = categorias
        self.telaNotebook = None  
        self.setWindowTitle("Cadastro de Desktop")
        self.setGeometry(100, 100, 300, 250)

        layout = QVBoxLayout()

        self.lblModelo = QLabel("Modelo:")
        self.txtModelo = QLineEdit()
        layout.addWidget(self.lblModelo)
        layout.addWidget(self.txtModelo)

        self.lblPreco = QLabel("Preço:")
        self.txtPreco = QLineEdit()
        layout.addWidget(self.lblPreco)
        layout.addWidget(self.txtPreco)

        self.lblCor = QLabel("Cor:")
        self.txtCor = QLineEdit()
        layout.addWidget(self.lblCor)
        layout.addWidget(self.txtCor)

        self.lblCategoria = QLabel("Categoria:")
        self.txtCategoria = QLineEdit()
        layout.addWidget(self.lblCategoria)
        layout.addWidget(self.txtCategoria)

        self.btnSalvar = QPushButton("Salvar")
        self.btnSalvar.clicked.connect(self.salvar)
        layout.addWidget(self.btnSalvar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def setTelaNotebook(self, telaNotebook):
        self.telaNotebook = telaNotebook

    def salvar(self):
        nova_categoria = self.txtCategoria.text().strip()
        if nova_categoria and nova_categoria not in self.categorias:
            self.categorias.append(nova_categoria)
            if self.telaNotebook:
                self.telaNotebook.carregarCategorias()
        print("Desktop salvo.")         
        self.close()

        
