from Abstract.Expresion import Expresion
from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Simbolo.Simbolo import Simbolo


class AsignacionStruct(Instruccion):
    def __init__(self, fila, columna, ids, expresion):
        super().__init__(fila, columna)
        self.ids = ids
        self.expresion = expresion

    def ejecutar(self, entorno):
        valor = self.expresion.ejecutar(entorno)
        simbolo = entorno.getVar(self.ids[0])

        if simbolo.mutable:
            for i in range(1, len(self.ids)):
                value = self.expresion.ejecutar(entorno)
                simbolo.valor.update({self.ids[i]: value})
                #print(f'Expre: {self.expresion.ejecutar(entorno)}')
                #print(f'id: {simbolo.valor.get(self.ids[i])}')
        else:
            print(f'Error_AsigStruct: La estructura no es mutable')

        tmp = simbolo.valor.get(self.ids[0])
        pass