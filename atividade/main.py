import sys
from PyQt5.QtWidgets import QApplication
from TelaNotebook import TelaNotebook
from TelaDesktop import TelaDesktop

if __name__ == "__main__":
    app = QApplication(sys.argv)

    categorias = []

   
    tela_notebook = TelaNotebook(categorias)
    tela_notebook.show()

   
    tela_desktop = TelaDesktop(categorias)
    tela_desktop.show()

    sys.exit(app.exec_())
