import ply.lex as lex
import re
import codecs
import os
import sys

tokens = [
    'ID',
    'STRLIT',
    'CHARLIT',
    'NUMBER',
    'DECIMAL',
    'COMENT',
    'GUIONFLECHA',
    'ICOR',
    'DCOR',
    'ILLAVE',
    'DLLAVE',
    'IPAR',
    'DPAR',
    'DOSPTOS',
    'COMA',
    'PTOCOMA',
    'MENORQ',
    'MAYORQ',
    'PUNTO',
    'IGUAL',
    'MAS',
    'MENOS',
    'MUL',
    'DIV',
    'MOD',
    'BARVER',
    'AMP',
    'ADM',
    'RQUEST',
    'MYRIGUAL',
    'MNRIGUAL',
    'DOBIGUAL',
    'ADMIGUAL',
    'DOBARVER',
    'DOBAMP',
    'RSTR'
]

reservadas = {
    'i64': 'i64',
    'f64': 'f64',
    'bool': 'bool',
    'char': 'char',
    'string': 'String',
    #'&str': 'str',
    'usize': 'usize',
    'let': 'let',
    'mut': 'mut',
    'struct': 'struct',
    'as': 'as',
    'println!': 'println',
    'true': 'true',
    'false': 'false',
    'fn': 'fn',
    'abs': 'abs',
    'sqrt': 'sqrt',
    'to_string': 'tostring',
    'clone': 'clone',
    'new': 'new',
    'len': 'len',
    'push': 'push',
    'remove': 'remove',
    'contains': 'contains',
    'insert': 'insert',
    'capacity': 'capacity',
    'with_capacity': 'withcapacity',
    'return': 'return',
    'continue': 'continue',
    'break': 'break',
    'main': 'main',
    'if': 'if',
    'else': 'else',
    'else if': 'elseif',
    'while': 'while',
    'loop': 'loop',
    'i64::pow': 'i64pow',
    'f64::powf': 'i64powf'
}

tokens = tokens+list(reservadas.values())

t_RSTR = '&str'
t_GUIONFLECHA = r'\->'
t_MAS = r'\+'
t_MENOS = r'\-'
t_MUL = r'\*'
t_DIV = r'\/'
t_MOD = r'\%'
t_ICOR = r'\['
t_DCOR = r'\]'
t_ILLAVE = r'\{'
t_DLLAVE = r'\}'
t_IPAR = r'\('
t_DPAR = r'\)'
t_DOSPTOS = r':'
t_COMA = r','
t_PTOCOMA = r';'
t_MENORQ = r'<'
t_MAYORQ = r'>'
t_PUNTO = r'\.'
t_IGUAL = r'='
t_BARVER = r'\|'
t_AMP = r'&'
t_ADM = r'!'
t_RQUEST = r'\?'
t_MYRIGUAL = r'>='
t_MNRIGUAL = r'<='
t_DOBIGUAL = r'=='
t_ADMIGUAL = r'!='
t_DOBARVER = r'\|\|'
t_DOBAMP = r'&&'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reservadas:
        t.value = t.value
        t.type = reservadas.get(t.value.lower(), 'ID')
        print(f'tvalue: {t.value}, ttype: {t.type}')
    return t

def t_COMENT(t):
    r'//.*\n'
    t.lexer.lineno += 1

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_STRLIT(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas dobles
    return t

def t_CHARLIT(t):
    r'\'.*?\''
    t.value = t.value[1:-1] # remuevo las comillas simples
    return t

def t_error(t):
    print("caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Asociación de operadores y precedencia
precedence = (
    ('left','MAS','MENOS'),
    ('left','MUL','DIV'),
    ('right','UMENOS'),
    )

f = open("./entrada1.txt", "r")
input = f.read()
analizador = lex.lex()
analizador.input(input)

while True:
	tok = analizador.token()
	if not tok : break
	print(tok)