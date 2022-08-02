import ply.yacc as yacc
from aLexico import tokens, analizador

# Asociación de operadores y precedencia
precedence = (
    #('left','CONCAT'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MUL', 'DIV', 'MOD'),
    ('right', 'UMENOS'),
)

# Inicio sintáctico
