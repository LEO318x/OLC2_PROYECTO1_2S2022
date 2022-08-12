from Abstract.Instruccion import Instruccion


class Match(Instruccion):
    def __init__(self, fila, columna):
        super().__init__(fila, columna)

    def ejecutar(self, entorno):
        pass