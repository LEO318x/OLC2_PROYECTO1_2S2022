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
    STRUCT = 10
    BREAK = 11
    CONTINUE = 12
    RETURN = 13
    RSTR = 14

class TIPO_OPERACION(Enum):
    SUMA = 1
    RESTA = 2
    MULTI = 3
    DIV = 4
    MOD = 5
    EXPO = 6

'''class TIPO_RETORNO(Enum):
    INTEGER = 1
    FLOAT = 2
    CHAR = 3
    STRING = 4
    ID = 5
    BOOL = 6
    NULL = 7
    ARRAY = 8
    VECT = 9'''

class TIPO_RELACIONAL(Enum):
    IGUALACION = 1
    NOIGUAL = 2
    MENOR = 3
    MENORIGUAL = 4
    MAYOR = 5
    MAYORIGUAL = 6
    DISTINTO = 7

class TIPO_LOGICO(Enum):
    AND = 1
    OR = 2
    NOT = 3

