from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QVBoxLayout, QPushButton, QComboBox, QWidget

class TelaNotebook(QMainWindow):
    def __init__(self, categorias):
        super().__init__()
        self.categorias = categorias
        self.setWindowTitle("Cadastro de Notebook")
        self.setGeometry(500, 100, 300, 250)

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
        self.cmbCategoria = QComboBox()
        layout.addWidget(self.lblCategoria)
        layout.addWidget(self.cmbCategoria)

        self.btnSalvar = QPushButton("Salvar")
        self.btnSalvar.clicked.connect(self.salvar)
        layout.addWidget(self.btnSalvar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.carregarCategorias()

    def carregarCategorias(self):
        self.cmbCategoria.clear()
        self.cmbCategoria.addItem("Selecione...", None)
        for cat in self.categorias:
            self.cmbCategoria.addItem(cat)

    def salvar(self):
        print("Notebook salvo.")
