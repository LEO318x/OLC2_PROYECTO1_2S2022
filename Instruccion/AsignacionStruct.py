from Abstract.Expresion import Expresion
from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Simbolo.Simbolo import Simbolo
from Simbolo.Tipo import TIPO_DATO


class AsignacionStruct(Instruccion):
    def __init__(self, fila, columna, ids, expresion):
        super().__init__(fila, columna)
        self.ids = ids
        self.expresion = expresion

    def ejecutar(self, entorno):
        print(f'ids{self.ids}')
        valor = self.expresion.ejecutar(entorno)
        simbolo = entorno.getVar(self.ids[0])
        if simbolo.mutable:
            #print(f'{simbolo.valor}')
            #while True:
                for clave, valor in simbolo.valor.items():
                    print(f'clave {clave}, valor.v {valor.tipo}')
                    if valor.tipo == TIPO_DATO.STRUCT:
                        simbolo = valor

            # print(f'simb: {valor}, {valor.valor}, {valor.tipo}')
            # self.ids.pop(0)
            # obj = simbolo.valor.get(self.ids.pop(0))
            # while True:
            #     print(f'ids{self.ids}')
            #     if obj.tipo == TIPO_DATO.STRUCT:
            #         print(f'obj: {obj.valor}, objt: {obj.tipo}')
            #             if len(self.ids) == 1:
            #
            #         break
            #     else:
            #         break
            #
            # # for i in range(1, len(self.ids)):
            # #     #while True:
            # #     print(f'id: {self.ids[i]}')
            # #     obj = simbolo.valor.get(self.ids[i])
            # #     print(f'obj: {obj}')
            #
            # #     obj = simbolo.valor.get(self.ids[i])
            # #     if obj.tipo == TIPO_DATO.STRUCT:
            # #         tmp = simbolo.valor.get(self.ids[i])
            # #         value = self.expresion.ejecutar(entorno)
            # #         tmp.valor.update({self.ids[i]: value})
            # #         print(f'tmp: {tmp.valor}')

        else:
            print(f'Error_AsigStruct: La estructura no es mutable')
        pass