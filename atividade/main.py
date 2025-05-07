from PyQt5.QtWidgets import QApplication
from TelaDesktop import TelaDesktop
from TelaNotebook import TelaNotebook

if __name__ == '__main__':
    app = QApplication([])

    categorias = []

    tela_notebook = TelaNotebook(categorias)
    tela_desktop = TelaDesktop(categorias)
    tela_desktop.setTelaNotebook(tela_notebook)

    tela_desktop.show()
    tela_notebook.show()

    app.exec_()
