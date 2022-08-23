from Abstract.Instruccion import Instruccion
from Simbolo.Tipo import TIPO_DATO


class Print(Instruccion):

    def __init__(self, fila, columna, lexpression):
        super().__init__(fila, columna)
        self.lexpresion = lexpression

    def ejecutar(self, entorno):
        tmpls = self.lexpresion.copy()
        tmplsaux = self.lexpresion.copy()
        if len(tmpls) > 1:
            tmpexpr = tmpls[0].ejecutar(entorno)
            #print(f'imp_eje: {tmpexpr.valor}')
            if "{}" in tmpexpr.valor or "{:?}" in tmpexpr.valor:
                del tmpls[0]
                tmpprint = tmpexpr.valor
                lstemp = []
                for expresion in tmpls:
                    valor = expresion.ejecutar(entorno)
                    lstemp.append(valor.valor)
                    #print(f"{valor.valor}")
                try:
                    tmpls = tmplsaux
                    tmpprint = tmpexpr.valor.format(*lstemp)
                    print(f'{tmpprint}')
                except:
                    print(f'Error_Print: ¿¿¿Misma cantidad de expresiones y', "{}{:?} o tipo dato no coincide con {}{:?} ???")
            else:
                print(f'imp_error: Falta', "{} {:?}")
        else:
            for expresion in tmpls:
                valor = expresion.ejecutar(entorno)
                if valor.tipo != TIPO_DATO.STRUCT:
                    print(f"{valor.valor}")
                else:
                    print(f'Error al imprimir')