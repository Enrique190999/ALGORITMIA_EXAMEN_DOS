# # Algoritmia
# ## Práctica 11
# En esta práctica se resolverá el problema de los árboles binarios de búsqueda.
 
from copy import deepcopy as dp

class ArbolBusquedaOptimo:
    """
    Clase para árboles de búsquedas construidos a partir de las probabilidades
    de búsqueda de sus claves y pseudoclaves.
    Las pseudoclaves representan las búsquedas de elementos que no están en el
    árbol.
    """
    
    def __init__(self, claves, probab_claves, probab_pseudo = None):
        pass
        self.claves = claves
        self.altura = -1
        self.probab_claves = probab_claves
        
        if probab_pseudo is not None:
            self.pseudo = probab_pseudo
        else:
            self.pseudo = [(0) _ for in range(len(self.probab_claves) + 1)]
        
        self.__create_tables()
        self.__create_tree()
        
    def __create_tables(self):
        pass
        

    def __create_tree(self, from_=1, to_=None, root=None, altura = 0):
        pass
    
    def __search(self, clave=None):
        pass
        
    def __str__(self, clave=None):
        pass
        
    def __len__(self):
        pass
        
    def __contains__(self, clave):
        pass
    
    def __getitem__(self, i):
        pass

    def raiz(self):
        pass
        
    def profundidad(self, clave=None):
        pass
        
    def hijos(self, clave=None):
        pass
    
    def coste_esperado(self, clave=None):
        pass