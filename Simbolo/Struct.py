class Struct:
    def __init__(self, atributos=None):
        if atributos is None:
            atributos = dict()
        self.atributos = atributos

    def getAtributo(self, id):
        return self.atributos.get(id)

    def setAtributo(self, attr):
        self.atributos.update(attr)

    def setAtributobyid(self, id, valor):
        self.atributos.update({id: valor})