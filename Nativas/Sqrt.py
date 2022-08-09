import math

from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Simbolo.Tipo import TIPO_DATO


class Sqrt(Instruccion):
    def __init__(self, fila, columna, expresion):
        super().__init__(fila, columna)
        self.expresion = expresion

    def ejecutar(self, entorno):
        expr = self.expresion.ejecutar(entorno)
        if expr.valor > 0:
            if expr.tipo == TIPO_DATO.FLOAT:
                return Retorno(math.sqrt(expr.valor), TIPO_DATO.FLOAT)
            else:
                print(f'Error_Sqrt: No se puede operar')
                return Retorno(0, TIPO_DATO.INTEGER)
        else:
            print(f'Error_Sqrt: No se puede operar número negativo en raíz')
            return Retorno(0, TIPO_DATO.INTEGER)
