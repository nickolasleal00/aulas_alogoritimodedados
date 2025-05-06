from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QVBoxLayout, QPushButton, QWidget

class TelaDesktop(QMainWindow):
    def __init__(self, categorias):
        super().__init__()
        self.categorias = categorias  
        self.setWindowTitle("Cadastro de Desktop")
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
        self.txtCategoria = QLineEdit()
        layout.addWidget(self.lblCategoria)
        layout.addWidget(self.txtCategoria)

      
        btnSalvar = QPushButton("Salvar")
        btnSalvar.clicked.connect(self.salvar)
        layout.addWidget(btnSalvar)

     
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def salvar(self):
        modelo = self.txtModelo.text()
        cor = self.txtCor.text()
        preco = self.txtPreco.text()
        categoria = self.txtCategoria.text()

        if modelo != "" and cor != "" and preco != "" and categoria != "":
        
            print(f"Desktop Salvo: Modelo = {modelo}, Cor = {cor}, Preço = {preco}, Categoria = {categoria}")
            
         
            if categoria not in self.categorias:
                self.categorias.append(categoria)

          
            self.atualizarTelaNotebook()

            self.close()

    def atualizarTelaNotebook(self):
      
        if hasattr(self, 'telaNotebook'):
            self.telaNotebook.carregarCategorias()
