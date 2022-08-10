from Abstract.Instruccion import Instruccion
from Simbolo.Tipo import TIPO_DATO


class Print(Instruccion):

    def __init__(self, lexpression):
        self.lexpresion = lexpression

    def ejecutar(self, entorno):
        if len(self.lexpresion) > 1:
            for expresion in self.lexpresion:
                if valor.tipo == TIPO_DATO.RSTR:
                    valor = expresion.ejecutar(entorno)
                    print(f"{valor.valor}")
        else:
            for expresion in self.lexpresion:
                valor = expresion.ejecutar(entorno)
                print(f"{valor.valor}")