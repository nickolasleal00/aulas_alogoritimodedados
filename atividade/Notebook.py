from Produto import Produto

class Notebook(Produto):
    def __init__(self, tempoDeBateria):
        self.__tempoDeBateria = tempoDeBateria