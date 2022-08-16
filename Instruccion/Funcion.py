from Abstract.Instruccion import Instruccion


class Funcion(Instruccion):
    def __init__(self, fila, columna, id, instruccion, parametros, tipo_retorno=None):
        super().__init__(fila, columna)
        self.id = id
        self.sentencia = instruccion
        self.parametros = parametros
        self.tipo_retorno = tipo_retorno

    def ejecutar(self, entorno):
        # print(f'funcion_ejec {self.parametros}')
        entorno.guardarFuncion(self.id, self)
