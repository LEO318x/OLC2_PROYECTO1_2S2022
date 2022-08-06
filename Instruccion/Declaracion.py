from Abstract.Instruccion import Instruccion


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
