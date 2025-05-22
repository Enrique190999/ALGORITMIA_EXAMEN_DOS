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
        self.p = probab_claves
        
        if probab_pseudo is not None:
            self.pseudo = probab_pseudo
        else:
            self.pseudo = [(0) for _ in range (len(self.p) + 1)]
        
        self.__create_tables()
        self.__create_tree()
        
    def __create_tables(self):
        pass
        n = len(self.p)
        self.e = [[(0) * (n+1)] for _ in range(n+1)]
        self._raiz = [[(0) * (n+1)] for _ in range(n+1)]
        self.w = [[(0) * (n+1)] for _ in range(n+1)]
        
        for i in range(1,n+1):
            self.e[i][i] = self.pseudo[i]
            self.w[i][i] = self.pseudo[i]
        
        for long_actual in range(1,n+1):
            for inicio in range(0,n-long_actual + 1):
                fin = inicio + long_actual
                
                self.w[inicio][fin] = (
                    self.w[inicio][fin-1] + 
                    self.p[fin - 1] +
                    self.pseudo[fin]
                )
                
                self.e[inicio][fin] = float('inf')
                
                for punto_medio in range(1+inicio, 1+fin):
                    self.e[inicio][fin] = (
                        self.e[inicio][punto_medio - 1] + 
                        self.e[punto_medio][fin] + 
                        self.w[inicio][fin]
                    )
            
    def __create_tree(self, from_=1, to_=None, root=None, altura = 0):
        pass
        if root is None:
            root = {}
            self.root = root
        
        if to_ is not None and from_ > to_:
            return None
        
        if to_ is None:
            to_ = len(self.p)
        
        if altura > self.altura:
            self.altura = altura
        
        i = from_ - 1
        j = to_
        
        if i >= to_:
            return None
        
        r = self.raiz[i][j]
        root['v'] = r
        root['k'] = self.claves[r-1]
        root['h'] = altura
        root['coste'] = self.e[i][j]
        root['izq'] = self.__create_tree(from_,r-1,{}, altura + 1)
        root['der'] = self.__create_tree(r+1,to_,{},altura + 1)
        return root
    
    def __search(self, clave=None):
        if clave is None:
            return self.root
        
        root = self.root
        valor = int(clave[1:])
        
        while True:
            if root is None:
                return None
            
            if root['v'] == valor:
                return root
            
            if root['v'] < valor:
                root = root['der'] if root['der'] is not None else None
            else:
                root = root['izq'] if root['izq'] is not None else None
        pass
        
    def __str__(self, clave=None):
        
        root = self.__search(clave)
        izq = self.__str__(root['izq']['k']) if root['izq'] is not None else None
        der = self.__str__(root['der']['k']) if root['der'] is not None else None
        r = root['k']
        
        return f"({izq}{r}{der})" 
        pass
        
    def __len__(self):
        return len(self.claves)
        pass
        
    def __contains__(self, clave):
        pass
        return self.__search(clave) is not None
    
    def __getitem__(self, i):
        
        return self.claves[i]
        pass

    def raiz(self):
        return self.root['k']
        pass
        
    def profundidad(self, clave=None):
        if clave is None:
            return None
        return self.__search(clave)['h']
    
        pass
        
    def hijos(self, clave=None):
        root = self.__search(clave)
        
        if root is None:
            return None
        else:
            izq = root['izq']['k'] if root['izq'] is not None else None
            der = root['der']['k'] if root['der'] is not None else None
            return(izq,der)
        
        pass
    
    def coste_esperado(self, clave=None):
        return self.__search(clave)['coste']
        pass