from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QVBoxLayout, QPushButton, QComboBox, QWidget

class TelaNotebook(QMainWindow):
    def __init__(self, categorias):
        super().__init__()
        self.categorias = categorias  
        self.setWindowTitle("Cadastro de Notebook")
        self.setGeometry(200, 100, 300, 250)

      
        layout = QVBoxLayout()

       
        self.lblModelo = QLabel("Modelo:")
        self.txtModelo = QLineEdit()
        layout.addWidget(self.lblModelo)
        layout.addWidget(self.txtModelo)

      
        self.lblCor = QLabel("Cor:")
        self.txtCor = QLineEdit()
        layout.addWidget(self.lblCor)
        layout.addWidget(self.txtCor)

       
        self.lblPreco = QLabel("Preço:")
        self.txtPreco = QLineEdit()
        layout.addWidget(self.lblPreco)
        layout.addWidget(self.txtPreco)

       
        self.lblCategoria = QLabel("Categoria:")
        self.cmbCategoria = QComboBox()
        self.carregarCategorias()
        layout.addWidget(self.lblCategoria)
        layout.addWidget(self.cmbCategoria)

       
        btnSalvar = QPushButton("Salvar")
        btnSalvar.clicked.connect(self.salvar)
        layout.addWidget(btnSalvar)

      
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def carregarCategorias(self):
       
        self.cmbCategoria.clear()
        self.cmbCategoria.addItem("Selecione...", None)
        for cat in self.categorias:
            self.cmbCategoria.addItem(cat, cat)

    def salvar(self):
        modelo = self.txtModelo.text()
        cor = self.txtCor.text()
        preco = self.txtPreco.text()
        categoria = self.cmbCategoria.currentText()

        if modelo != "" and cor != "" and preco != "" and categoria != "Selecione...":
           
            print(f"Notebook Salvo: Modelo = {modelo}, Cor = {cor}, Preço = {preco}, Categoria = {categoria}")
            self.close()
