import ply.yacc as yacc
from Expresion.Acceso import Acceso
from Expresion.Logica import Logica
from Expresion.Relacional import Relacional
from Instruccion.Asignacion import Asignacion
from Instruccion.Casteo import Casteo
from Instruccion.Declaracion import Declaracion, Declaracion_Tipo
from Instruccion.Loop import Loop
from Instruccion.Sentencia import Sentencia
from Nativas.Abs import Abs
from Nativas.Exponente import Exponente
from Nativas.Sqrt import Sqrt
from Nativas.ToOwned import ToOwned
from Nativas.ToString import ToString
from Simbolo.Entorno import Entorno
from aLexico import tokens, analizador, find_column
from Instruccion.Imprimir import Print
from Instruccion.If import If
from Instruccion.While import While
from Instruccion.Break import Break
from Instruccion.Continue import Continue
from Expresion.Literal import Literal
from Simbolo.Tipo import *
from Expresion.Aritmetica import Aritmetica

# Asociación de operadores y precedencia
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NEGA'),
    ('left', 'IGUALACION', 'DISTINTO'),
    ('left', 'MENORQ', 'MAYORQ', 'MYRIGUAL', 'MNRIGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MUL', 'DIV', 'MOD'),
    ('left', 'IPAR', 'DPAR'),
    ('right', 'UMENOS'),
)


# Inicio sintáctico
def p_init(t):
    'init : instrucciones'
    t[0] = t[1]


def p_lista_instrucciones(t):
    'instrucciones : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t):
    'instrucciones : instruccion'
    t[0] = [t[1]]


def p_instruccion(t):
    '''instruccion : declaracion
                  | declaracion_con_tipo
                  | asignacion
                  | ifst
                  | whilest
                  | loopst
                  | print_inst
                  | breakinst
                  | continueinst'''
    t[0] = t[1]


def p_declaracion(t):
    '''declaracion : LET ID IGUAL expresion PTOCOMA
                   | LET MUT ID IGUAL expresion PTOCOMA'''
    if t.slice[2].type == 'MUT':
        t[0] = Declaracion(t[3], t[5], True, t.lineno(4), find_column(input, t.slice[4]))
    else:
        t[0] = Declaracion(t[2], t[4], False, t.lineno(3), find_column(input, t.slice[3]))


def p_declaracion_con_tipo(t):
    '''declaracion_con_tipo : LET ID DOSPTOS tipo_dato IGUAL expresion PTOCOMA
                            | LET MUT ID DOSPTOS tipo_dato IGUAL expresion PTOCOMA'''
    if t.slice[2].type == 'MUT':
        t[0] = Declaracion_Tipo(t[3], t[7], t[5], True, t.lineno(6), find_column(input, t.slice[6]))
    else:
        t[0] = Declaracion_Tipo(t[2], t[6], t[4], False, t.lineno(5), find_column(input, t.slice[5]))


def p_tipo_dato(t):
    '''tipo_dato : I64
                 | F64
                 | STRING
                 | RSTR
                 | CHAR
                 | BOOL'''
    tipo = ""
    match t[1]:
        case 'i64':
            tipo = TIPO_DATO.INTEGER
        case 'f64':
            tipo = TIPO_DATO.FLOAT
        case 'bool':
            tipo = TIPO_DATO.BOOL
        case 'String':
            tipo = TIPO_DATO.STRING
        case '&str':
            tipo = TIPO_DATO.RSTR
        case 'char':
            tipo = TIPO_DATO.CHAR
    t[0] = tipo


def p_asignacion(t):
    '''asignacion : ID IGUAL expresion PTOCOMA'''
    t[0] = Asignacion(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))


def p_ifst(t):
    '''ifst : IF expresion st elsest'''
    #print(f'g_if{t[3]}')
    t[0] = If(t.lineno(1), find_column(input, t.slice[1]), t[2], t[3], t[4])


def p_elsest(t):
    '''elsest : ELSE st
              | ELSE ifst
              | '''

    if len(t) > 1:
        t[0] = t[2]
    else:
        t[0] = None


def p_whilest(t):
    '''whilest : WHILE expresion st '''
    t[0] = While(t.lineno(1), find_column(input, t.slice[1]), t[2], t[3])

def p_loopst(t):
    '''loopst : LOOP st'''
    t[0] = Loop(t.lineno(1), find_column(input, t.slice[1]), t[2])


def p_breakinst(t):
    '''breakinst : BREAK PTOCOMA'''
    t[0] = Break(t.lineno(1), find_column(input, t.slice[1]))

def p_continueinst(t):
    '''continueinst : CONTINUE PTOCOMA'''
    t[0] = Continue(t.lineno(1), find_column(input, t.slice[1]))

def p_st(t):
    '''st : ILLAVE instrucciones DLLAVE
          | ILLAVE DLLAVE'''
    # print(f't[2]: {t.slice[2].type}')
    if t.slice[2].type == 'instrucciones':
        t[0] = Sentencia(t.lineno(1), find_column(input, t.slice[1]), t[2])
    else:
        t[0] = Sentencia(t.lineno(1), find_column(input, t.slice[1]), None)


def p_print(t):
    '''print_inst : PRINTLN NOT IPAR lexpresion DPAR PTOCOMA'''

    instr = Print(t[4])
    t[0] = instr

def p_lprint(t):
    '''lexpresion : lexpresion COMA expresion'''
    t[1].append(t[3])
    t[0] = t[1]


def p_lprinto(t):
    '''lexpresion : expresion'''
    t[0] = [t[1]]

def p_expresion_aritmetica(t):
    '''expresion : expresion MAS expresion
                | expresion MENOS expresion
                | expresion MUL expresion
                | expresion DIV expresion
                | expresion MOD expresion
                | I64 DOSPTOS DOSPTOS POW IPAR expresion COMA expresion DPAR
                | F64 DOSPTOS DOSPTOS POWF IPAR expresion COMA expresion DPAR '''

    if t[2] == '+':
        # print(f'|--->{t[1]}')
        t[0] = Aritmetica(t[1], TIPO_OPERACION.SUMA, t[3], t.lineno(2), find_column(input, t.slice[2]), None)
    elif t[2] == '-':
        t[0] = Aritmetica(t[1], TIPO_OPERACION.RESTA, t[3], t.lineno(2), find_column(input, t.slice[2]), None)
    elif t[2] == '*':
        t[0] = Aritmetica(t[1], TIPO_OPERACION.MULTI, t[3], t.lineno(2), find_column(input, t.slice[2]), None)
    elif t[2] == '/':
        t[0] = Aritmetica(t[1], TIPO_OPERACION.DIV, t[3], t.lineno(2), find_column(input, t.slice[2]), None)
    elif t[2] == '%':
        t[0] = Aritmetica(t[1], TIPO_OPERACION.MOD, t[3], t.lineno(2), find_column(input, t.slice[2]), None)
    elif t.slice[4].type == 'POW':
        t[0] = Exponente(t[6], TIPO_OPERACION.EXPO, t[8], t.lineno(5), find_column(input, t.slice[5]))
    elif t.slice[4].type == 'POWF':
        t[0] = Exponente(t[6], TIPO_OPERACION.EXPO, t[8], t.lineno(5), find_column(input, t.slice[5]))


def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec UMENOS'
    t[0] = Aritmetica(None, None, t[2], t.lineno(1), find_column(input, t.slice[1]), True)


def p_expresion_agrupacion(t):
    'expresion : IPAR expresion DPAR'
    t[0] = t[2]


def p_expresion_relacional(t):
    '''expresion : expresion MAYORQ expresion
                        | expresion MENORQ expresion
                        | expresion MYRIGUAL expresion
                        | expresion MNRIGUAL expresion
                        | expresion IGUALACION expresion
                        | expresion DISTINTO expresion'''
    if t.slice[2].type == 'MAYORQ':
        t[0] = Relacional(t[1], TIPO_RELACIONAL.MAYOR, t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t.slice[2].type == 'MENORQ':
        t[0] = Relacional(t[1], TIPO_RELACIONAL.MENOR, t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t.slice[2].type == 'MYRIGUAL':
        t[0] = Relacional(t[1], TIPO_RELACIONAL.MAYORIGUAL, t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t.slice[2].type == 'MNRIGUAL':
        t[0] = Relacional(t[1], TIPO_RELACIONAL.MENORIGUAL, t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t.slice[2].type == 'IGUALACION':
        t[0] = Relacional(t[1], TIPO_RELACIONAL.IGUALACION, t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t.slice[2].type == 'DISTINTO':
        t[0] = Relacional(t[1], TIPO_RELACIONAL.DISTINTO, t[3], t.lineno(2), find_column(input, t.slice[2]))


def p_expresion_logica(t):
    '''expresion : expresion AND expresion
                 | expresion OR expresion
                 | NOT expresion %prec NEGA'''
    # print(f'gtipo: {t.slice[2].type}, gvalor {t[1]}')
    if t.slice[2].type == 'AND':
        t[0] = Logica(t[1], TIPO_LOGICO.AND, t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t.slice[2].type == 'OR':
        t[0] = Logica(t[1], TIPO_LOGICO.OR, t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t.slice[1].type == 'NOT':
        t[0] = Logica(None, TIPO_LOGICO.NOT, t[2], t.lineno(1), find_column(input, t.slice[1]))


def p_expresion_casteo_primitiva(t):
    '''expresion : expresion AS tipo_dato '''
    t[0] = Casteo(t.lineno(2), find_column(input, t.slice[2]), t[3], t[1])


def p_expresion_tostring(t):
    '''expresion : expresion PUNTO TO_STRING IPAR DPAR'''
    t[0] = ToString(t.lineno(2), find_column(input, t.slice[2]), t[1])

def p_expresion_toowned(t):
    '''expresion : expresion PUNTO TO_OWNED IPAR DPAR'''
    t[0] = ToOwned(t.lineno(2), find_column(input, t.slice[2]), t[1])

def p_expresion_abs(t):
    '''expresion : expresion PUNTO ABS IPAR DPAR'''
    t[0] = Abs(t.lineno(2), find_column(input, t.slice[2]), t[1])

def p_expresion_sqrt(t):
    '''expresion : expresion PUNTO SQRT IPAR DPAR'''
    t[0] = Sqrt(t.lineno(2), find_column(input, t.slice[2]), t[1])


def p_expresion_primitiva(t):
    '''expresion : NUMBER
                | DECIMAL
                | ID
                | STRLIT
                | CHARLIT
                | TRUE
                | FALSE '''

    # print(f'gtipo: {t.slice[1].type}, gvalor {t[1]}')
    if t.slice[1].type == 'NUMBER':
        # print(f'Linea: {t.lineno(1)}, Columna: {find_column(input, t.slice[1])}')
        t[0] = Literal(t[1], TIPO_DATO.INTEGER, t.lineno(1), find_column(input, t.slice[1]))
    elif t.slice[1].type == 'DECIMAL':
        t[0] = Literal(t[1], TIPO_DATO.FLOAT, t.lineno(1), find_column(input, t.slice[1]))
    elif t.slice[1].type == 'ID':
        t[0] = Acceso(t[1], t.lineno(1), find_column(input, t.slice[1]))
    elif t.slice[1].type == 'STRLIT':
        t[0] = Literal(t[1], TIPO_DATO.RSTR, t.lineno(1), find_column(input, t.slice[1]))
    elif t.slice[1].type == 'CHARLIT':
        t[0] = Literal(t[1], TIPO_DATO.CHAR, t.lineno(1), find_column(input, t.slice[1]))
    elif t.slice[1].type == 'TRUE':
        t[0] = Literal(t[1], TIPO_DATO.BOOL, t.lineno(1), find_column(input, t.slice[1]))
    elif t.slice[1].type == 'FALSE':
        t[0] = Literal(t[1], TIPO_DATO.BOOL, t.lineno(1), find_column(input, t.slice[1]))


def p_empty(t):
    'empty :'
    pass

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)


# Parser
parser = yacc.yacc()


def analizar(entrada):
    resultado = parser.parse(entrada)
    for i in resultado:
        i.ejecutar(None)


if __name__ == '__main__':
    f = open("./entrada1.txt", "r")

    input = f.read()
    resultado = parser.parse(input)
    env = Entorno(None)
    for i in resultado:
        i.ejecutar(env)
