from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Simbolo.Tipo import TIPO_DATO


class AccesoArreglo(Expresion):
    def __init__(self, fila, columna, anterior, indice):
        super().__init__(fila, columna)
        self.anterior = anterior
        self.indice = indice

    def ejecutar(self, entorno):

        anterior = self.anterior.ejecutar(entorno)
        #print(f'anterior: {anterior.valor}')
        if anterior.tipo != TIPO_DATO.ARRAY:
            print(f'Acceso_Arreglo_Error: No es un arreglo')
            return Retorno("Error", TIPO_DATO.ERROR)
        indice = self.indice.ejecutar(entorno)
        #print(f'Acceso_Arreglo: anterior {anterior.valor}')
        if indice.tipo != TIPO_DATO.INTEGER:
            print(f'Acceso_Arreglo_Error: El indice no es númerico')
            return Retorno("Error", TIPO_DATO.ERROR)
        if indice.valor < anterior.valor.getTamanio():
            valor = anterior.valor.getAtributo(indice.valor)
        else:
            print(f'Acceso_Arreglo_Error: Indice del arreglo fuera de los límites')
            return Retorno("Error", TIPO_DATO.ERROR)
        return Retorno(valor.valor, valor.tipo)