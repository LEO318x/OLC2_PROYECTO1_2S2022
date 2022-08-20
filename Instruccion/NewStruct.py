import copy
from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Simbolo.Tipo import TIPO_DATO


class NewStruct(Instruccion):
    def __init__(self, fila, columna, id, struct):
        super().__init__(fila, columna)
        self.nombre = id
        self.struct = struct

    def ejecutar(self, entorno):
        valor = self.struct
        #defStruct = copy(entorno.getDefEstructura(self.nombre))
        defStruct = copy.deepcopy(entorno.getDefEstructura(self.nombre))
        latributos = defStruct.getLisAtributo()
        #print(f'NewStruct_ejec: {defStruct.getLisAtributo().get("name").valor}')
        #print(f'NewStruct_ejec: viene{len(valor)}, org:{len(latributos)}')
        if len(latributos) == len(valor):
            #print(f'{latributos}')

            for v in valor:
                tmp = v.popitem()
                ident = tmp[0]
                value = tmp[1].ejecutar(entorno)
                #print(f'ident: {ident}, valor:{value.valor} tipo: {value.tipo}')
                if ident in latributos:
                    svalue = latributos.get(ident)
                    #print(f'svalue: {type(svalue.tipo)}')
                    if value.tipo == svalue.tipo:
                        #print(f'newstruct: {value.tipo}')
                        latributos.update({ident: value})
                    else:
                        print(f'Error_NewStruct_Tipo: El tipo no coincide con el definido en la estructura')
                        print(f'{value.tipo}, {svalue.tipo}')
                        return
                else:
                    print(f'Error_NewStruct_Par: El nombre no coincide con el definido en la estructura')
                    return
            return Retorno(latributos, TIPO_DATO.STRUCT)
            #for v in valor:
            #    tmp = v.popitem()
            #    print(f'va{tmp[1].ejecutar(entorno).valor}')
            #for key in latributos:
            #    tipo = latributos.get(key)
            #    print(f'xdddd{tipo}')
        else:
            print(f'Error_NewStruct_Par: Faltan parametros en la estructura')
