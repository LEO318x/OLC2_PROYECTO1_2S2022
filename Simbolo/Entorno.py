# from Tipo import TIPO_DATO
from Simbolo.Simbolo import Simbolo


class Entorno:
    def __init__(self, anterior=None):
        self.variables = {}
        '''self.variables = {"a": Simbolo('a', 5, TIPO_DATO.INTEGER, False),
                          "b": Simbolo('b', 10, TIPO_DATO.INTEGER, False)}'''
        self.funciones = dict()
        self.anterior = anterior

    def guardar(self, id, valor, tipo, mutable):
        env = self
        #print(f'Env->{id, valor, tipo}')
        while env != None:
            if id in env.variables:
                env.variables.update({id: Simbolo(id, valor, tipo, mutable)})
                return
            env = env.anterior
        self.variables.update({id: Simbolo(id, valor, tipo, mutable)})
        #print(f'Ent_var: {self.variables}')

    def getVar(self, id):
        env = self
        #print(f'Env_getvar-> {id}, {env.variables}')
        while env != None:
            if id in env.variables:
                return env.variables.get(id)
            env = env.anterior
        return None

