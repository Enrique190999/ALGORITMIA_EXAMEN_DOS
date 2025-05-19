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
        n = len(self.p)
        # E = coste esperado, W = peso acumulado, R = raíz óptima
        self.e = [[0]*(n+1) for _ in range(n+1)]
        self.w = [[0]*(n+1) for _ in range(n+1)]
        self.raiz_ = [[0]*(n+1) for _ in range(n+1)]

        # Caso base: subárbol vacío (entre Ki y Ki+1) → q[i]
        for i in range(n+1):
            self.e[i][i] = self.pseudo[i]
            self.w[i][i] = self.pseudo[i]

        # long = nº de claves del subproblema  (1 … n)
        for long in range(1, n+1):
            for i in range(0, n-long+1):
                j = i + long      # intervalo (Ki+1 … Kj)  ← j es inclusivo
                # Peso acumulado: todo lo que haya dentro + q[j]
                self.w[i][j] = (
                    self.w[i][j-1] + self.p[j-1] + self.pseudo[j]
                )
                self.e[i][j] = float("inf")

                # Probar todas las posibles raíces r  (i+1 … j)
                for r in range(i+1, j+1):
                    coste = (
                        self.e[i][r-1] +          # coste subárbol izquierdo
                        self.e[r][j]   +          # coste subárbol derecho
                        self.w[i][j]              # peso total
                    )
                    if coste < self.e[i][j]:
                        self.e[i][j] = coste
                        self.raiz_[i][j] = r      # guardamos la clave raíz óptima


    def __create_tree(self, from_=1, to_=None, root=None, altura = 0):

        if to_ is not None and from_ > to_:
            return None
        if to_ is None:
            to_ = len(self.p)
        if root is None:
            root = {}
            self.root = root          # atributo público con la raíz
        if altura > self.altura:
            self.altura = altura

        i = from_ - 1                 # 0-based
        j = to_                       # inclusive
        if i >= j:                    # subárbol vacío
            return None

        r = self.raiz_[i][j]          # índice 1-based de la clave raíz
        root["k"] = self.claves[r-1]  # clave
        root["v"] = r                 # posición 1-based (para __search)
        root["h"] = altura
        root["coste"] = self.e[i][j]

        root["izq"] = self.__create_tree(from_, r-1, {}, altura+1)
        root["der"] = self.__create_tree(r+1, to_, {}, altura+1)
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