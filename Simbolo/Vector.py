from Simbolo.Simbolo import Simbolo


class Vector:
    def __init__(self):
        self.valores = []
        self.tamanio_max = 0

    def getAtributo(self, index):
        return self.valores[index]

    def getAtributos(self):
        return self.valores

    def setAtributo(self, valor: Simbolo):
        self.tamanio_max += 1
        if len(self.valores) > self.tamanio_max:
            self.tamanio_max *= 2
        self.valores.append(valor)

    def setAtributoConIndex(self, index, valor: Simbolo):
        self.valores[index] = valor

    def setCapacidadMax(self, capacidad):
        self.tamanio_max = capacidad

    def remove(self, index):
        tmp = self.valores[index]
        del self.valores[index]
        return tmp

    def getTodo(self):
        return self.valores

    def getTamanio(self):
        return len(self.valores)

    def getTamanioMax(self):
        return self.tamanio_max

    def crear_vector(self, tamanio):
        self.tamanio_max = tamanio
        for i in range(0, tamanio):
            self.valores.append(None)

