from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Simbolo.Tipo import *


class Literal(Expresion):
    def __init__(self, valor, tipo, fila, columna):
        self.valor = valor
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno):
        #print(f'----->{self.tipo}')
        if self.tipo == TIPO_DATO.INTEGER:
            return Retorno(self.valor, TIPO_DATO.INTEGER)
        elif self.tipo == TIPO_DATO.FLOAT:
            return Retorno(self.valor, TIPO_DATO.FLOAT)
        elif self.tipo == TIPO_DATO.STRING:
            return Retorno(self.valor, TIPO_DATO.STRING)
        elif self.tipo == TIPO_DATO.BOOL:
            if self.valor == 'true':
                self.valor = True
            elif self.valor == 'false':
                self.valor = False

            return Retorno(self.valor, TIPO_DATO.BOOL)
