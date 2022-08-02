from enum import Enum


class TIPO_DATO(Enum):
    INTEGER = 1
    FLOAT = 2
    CHAR = 3
    STRING = 4
    ID = 5
    BOOL = 6
    NULL = 7
    ARRAY = 8
    VECT = 9
    BREAK = 10
    CONTINUE = 11


class Simbolo():
    def __init__(self, id, tipo, valor):
        self.id = id
        self.tipo = tipo
        self.valor = valor


class TablaDeSimbolos():
    def __init__(self, simbolos = {}):
        self.simbolos = simbolos

    def agregar(self, simbolo):
        self.simbolos[simbolo.id] = simbolo

    def obtener(self, id):
        if not id in self.simbolos:
            print('Error: variable', id, ' no definida.')
        return self.simbolos[id]

    def actualizar(self, simbolo):
        if not simbolo.id in self.simbolos:
            print('Error: variable', simbolo.id, ' no definida')
        else:
            self.simbolos[simbolo.id] = simbolo