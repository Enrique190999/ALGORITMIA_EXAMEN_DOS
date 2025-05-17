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
        """
        Constructor a partir de una secuencia con las claves, sus probabilidades 
        y las probabilidades de buscar elementos que no están.
        La longitud de claves y probab_claves tiene que ser la misma.
        Si probab_pseudo es None no se tienen en cuentas las búsquedas de 
        elementos que no están.
        Si prabab_pseudo no es None, su longitud debe ser la de claves más 1.
        """
        self.claves = claves
        self.altura = -1
        self.p = probab_claves
        if probab_pseudo is not None:
            self.pseudo = probab_pseudo
        else:
            self.pseudo = [0 for _ in range(len(self.p) + 1)]
        self.__create_tables()
        self.__create_tree()

    def __create_tables(self):
        """
        Crea las tablas de coste y raíz para el árbol óptimo.
        """
        n = len(self.p)
        e = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(n+1):
            e[i][i] = self.pseudo[i]
        w = dp(e)
        raiz = [[0 for _ in range(n)] for _ in range(n)]
        for l in range(1, n+1):
            for i in range(1, n-l+2):
                j = i + l - 1
                e[i-1][j] = float("inf")
                w[i-1][j] = w[i-1][j-1] + self.p[j-1] + self.pseudo[j]
                for r in range(i, j+1):
                    t = e[i-1][r-1] + e[r][j] + e[r][j] + w[i-1][j]
                    if t < e[i-1][j]:
                        e[i-1][j] = t
                        raiz[i-1][j-1] = r
        self.e = e
        self.raiz_ = raiz

    def __create_tree(self, from_=1, to_=None, root=None, altura = 0):

        if to_ is not None and from_ > to_:
            return None
        if to_ is None:
            to_ = len(self.p)
        if root is None:
            root = dict()
            self.root = root
        if altura > self.altura:
            self.altura = altura
        raiz = self.raiz_[from_-1][to_-1]
        root["k"] = self.claves[raiz-1]
        root["v"]=raiz
        root["h"]=altura
        root["coste"]=self.e[from_-1][to_]
        root["izq"] = self.__create_tree(from_, raiz-1, {}, altura+1)
        root["der"] = self.__create_tree(raiz+1, to_, {}, altura+1)
        return root
    
    def __search(self, clave=None):
        if clave is None:
            return self.root
        raiz = self.root
        value = int(clave[1:])
        while True:
            if raiz is None:
                return None
            elif clave == raiz['k']:
                return raiz
            else: 
                if value > raiz['v']:
                    raiz = raiz['der']
                else:
                    raiz = raiz['izq']
        

    def __str__(self, clave=None):
        """
        Devuelve una cadena con una representación del árbol.
        Si clave es distinto de None se obtiene la cadena para el subárbol con
        clave como raíz.
        La cadena correspondiente a un nodo con dos hijos es 
        "(" + str(subarbol_izq) + str(clave) + str(subarbol_der) + ")".
        Para un subárbol vacío la cadena correspondiente es vacía.
        Por ejemplo, un nodo hoja se representa como "(" + str(clave) + ")".
        """
        raiz = self.__search(clave)
        izq = self.__str__(clave=raiz['izq']["k"]) if raiz['izq'] is not None else ""
        der = self.__str__(clave=raiz['der']["k"]) if raiz['der'] is not None else ""
        r=raiz['k']
        return"("+izq+r+der+")"
    
    def __len__(self):
        """Número de claves en el árbol."""
        return len(self.claves)
        
    def __contains__(self, clave):
        """Indica si una clave está en el árbol."""
        raiz = self.__search(clave)
        return raiz is not None
    
    def __getitem__(self, i):
        """Devuelve la clave i-ésima."""
        return self.claves[i]

    def raiz(self):
        """Devuelve la clave de la raíz del árbol.""" 
        return self.root['k']
        
    def profundidad(self, clave=None):
        """
        Devuelve la profundidad del árbol si clave es None, si no devuelve la 
        profundidad de la clave. 
        Si la clave no está devuelve None.
        """
        if clave is None:
            return self.altura
        raiz = self.__search(clave)
        if raiz is None:
            return None
        else:
            return raiz['h']


    def hijos(self, clave=None):
        """
        Devuelve un par con las claves del hijo izquierdo y derecho.
        Si el argumento clave es None devuelve los hijos de la raíz.
        En el resultado, None indica que no tiene ese hijo.
        """
        raiz = self.__search(clave)
        if raiz is None:
            return None
        else:
            izq = raiz['izq']["k"] if raiz['izq'] is not None else None
            der = raiz['der']["k"] if raiz['der'] is not None else None
            return (izq, der)
    
    def coste_esperado(self, clave=None):
        """
        Devuelve el coste esperado de la búsqueda en el subárbol asociado a una
        clave.
        Si clave es None, devuelve el coste del árbol completo.
        """
        return self.__search(clave)["coste"]