from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Simbolo.Tipo import TIPO_DATO


class Abs(Instruccion):
    def __init__(self, fila, columna, expresion):
        super().__init__(fila, columna)
        self.expresion = expresion

    def ejecutar(self, entorno):
        expr = self.expresion.ejecutar(entorno)
        if expr.tipo == TIPO_DATO.INTEGER:
            return Retorno(abs(expr.valor), TIPO_DATO.INTEGER)
        elif expr.tipo == TIPO_DATO.FLOAT:
            return Retorno(abs(expr.valor), TIPO_DATO.FLOAT)
        else:
            print(f'Error_Abs: No se puede operar')
            return Retorno(0, TIPO_DATO.INTEGER)