from Abstract.Instruccion import Instruccion


class Print(Instruccion):

    def __init__(self, expression):
        self.expression = expression

    def ejecutar(self, entorno):

        valor = self.expression.ejecutar(entorno)
        print(f"{valor.valor}")