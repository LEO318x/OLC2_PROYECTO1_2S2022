from Abstract.Instruccion import Instruccion
from Simbolo.Tipo import TIPO_DATO


class Declaracion(Instruccion):
    def __init__(self, id, valor, mutable, fila, columna):
        super().__init__(fila, columna)
        self.id = id
        self.valor = valor
        self.mutable = mutable

    def ejecutar(self, entorno):
        val = self.valor.ejecutar(entorno)
        #print(f'Decla: {val.tipo}')
        entorno.guardar(self.id, val.valor, val.tipo, self.mutable)

class Declaracion_Tipo(Instruccion):
    def __init__(self, id, valor, tipo, mutable, fila, columna):
        super().__init__(fila, columna)
        self.id = id
        self.valor = valor
        self.tipo = tipo
        self.mutable = mutable

    def ejecutar(self, entorno):
        val = self.valor.ejecutar(entorno)
        #print(f'dec_tipo_ejec: {val.tipo}, -> {self.tipo}')
        if val.tipo == self.tipo:
            entorno.guardar_var_tipo(self.id, val.valor, self.tipo, self.mutable)
        else:
            print(f'Error_decla_tipo_ejecutar: La variable "{self.id}" a declarar no coincide con el tipo de dato')
        #print(f'Decla: {val.tipo}')

