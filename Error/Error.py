class Error:
    def __init__(self, linea, columna, tipo, mensaje):
        self.linea = linea
        self.columna = columna
        self.tipo = tipo
        self.mensaje = mensaje