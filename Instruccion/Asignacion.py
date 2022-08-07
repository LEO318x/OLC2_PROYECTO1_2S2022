from Abstract.Instruccion import Instruccion


class Asignacion(Instruccion):
    def __init__(self, id, valor, fila, columna):
        super().__init__(fila, columna)
        self.id = id
        self.valor = valor

    def ejecutar(self, entorno):
        val = self.valor.ejecutar(entorno)
        # print(f'Decla: {val.tipo}')
        entorno.asignar_var(self.id, val.valor, val.tipo)
