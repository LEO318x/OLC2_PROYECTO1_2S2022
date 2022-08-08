from Abstract.Instruccion import Instruccion
from Simbolo.Tipo import TIPO_DATO


class If(Instruccion):
    def __init__(self, fila, columna, condicion, codigo, instruccion_else = None):
        super().__init__(fila, columna)
        self.condidcion = condicion
        self.codigo = codigo
        self.instruccion_else = instruccion_else

    def ejecutar(self, entorno):
        condicion = self.condidcion.ejecutar(entorno)
        #print(f'If_ejec -> {condicion}, valor: {condicion.valor}, tipo: {condicion.tipo}')
        if condicion.tipo != TIPO_DATO.BOOL:
            print(f'Error_If: La condición no es booleana, fila: {self.fila}, columna: {self.columna}')

        #print(f'if_eject_cond_valor: {self.codigo.sentencias}')
        if condicion.valor and self.codigo.sentencias is not None:
            return self.codigo.ejecutar(entorno)
        else:
            if self.instruccion_else:
                return self.instruccion_else.ejecutar(entorno)

        # Falta el else