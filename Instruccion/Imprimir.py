import Simbolo.Arreglo
from Abstract.Instruccion import Instruccion
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Tipo import TIPO_DATO
from Recolector.Recolector import recolector
from Simbolo import Arreglo

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
                    if isinstance(valor.valor, Simbolo.Arreglo.Arreglo):
                        lstemp.append(self.imprimirArreglo(valor.valor))
                    else:
                        lstemp.append(valor.valor)
                try:
                    tmpls = tmplsaux
                    tmpprint = tmpexpr.valor.format(*lstemp)
                    recolector.append(str(tmpprint))
                    print(f'{tmpprint}')
                except:
                    lerrores.append(Error(self.fila, self.columna, entorno.nombre, f'Error_Print: ¿¿¿Misma cantidad de expresiones y ' + "{}{:?} o tipo dato no coincide con {}{:?} ???"))
                    print(f'Error_Print: ¿¿¿Misma cantidad de expresiones y', "{}{:?} o tipo dato no coincide con {}{:?} ???")
            else:
                lerrores.append(Error(self.fila, self.columna, entorno.nombre, f'imp_error: Falta', "{} {:?}"))
                print(f'imp_error: Falta', "{} {:?}")
        else:
            for expresion in tmpls:
                valor = expresion.ejecutar(entorno)
                if valor.tipo != TIPO_DATO.STRUCT:
                    if isinstance(valor.valor, Simbolo.Arreglo.Arreglo):
                        recolector.append(self.imprimirArreglo(valor.valor))
                        print(f"{self.imprimirArreglo(valor.valor)}")
                    else:
                        print(f"{valor.valor}")
                else:
                    lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'Error al imprimir'))
                    print(f'Error al imprimir')

    def imprimirArreglo(self, arreglo):
        tmp = "["
        auxCount = 0
        for x in arreglo.getAtributos():
            if isinstance(x.valor, Simbolo.Arreglo.Arreglo):
                ret = self.imprimirArreglo(x.valor)
                tmp += str(ret)
            else:
                if auxCount == arreglo.getTamanio() - 1:
                    tmp += str(x.valor)
                else:
                    tmp += str(x.valor) + ","
            auxCount += 1
        tmp += "]"
        return tmp