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
        self.claves = claves # Las claves a usar
        self.altura = -1 # La altura es -1 porque aun no se ha construido
        self.p = probab_claves # La probabilidad de las llaves
        
        """
        Si la lista de probabilidades de busqueda no es none la almacenamos en la variable del constructor, pseudo.
        Si lo es, creamos una litsa de 0 de tantos elementos como probabiliddes  + 1
        """
        if probab_pseudo is not None:
            self.pseudo = probab_pseudo
        else:
            self.pseudo = [0 for _ in range(len(self.p) + 1)]
        self.__create_tables()
        self.__create_tree()

    def __create_tables(self):
        """
        Instanciamos n como el número de probabilidades
        
        Ademas creamos las tablas de e,w y raiz, todas ellas que tendras tantos numero de probabilidades y contando el 0 de filas y columnas
        """
        n = len(self.p)
        self.e = [[0]*(n+1) for _ in range(n+1)]
        self.w = [[0]*(n+1) for _ in range(n+1)]
        self.raiz_ = [[0]*(n+1) for _ in range(n+1)]

        """
        Recorremos todas estas y almacenamos en las tables de e y de w en la diagonal el valor de las probabilidades de pseudo.
        """
        for i in range(n+1):
            self.e[i][i] = self.pseudo[i]
            self.w[i][i] = self.pseudo[i]

        """
        Una vez hecha las diagonales, recorremos por longitudes.
        exactamente igual el bucle que la multiplicación de matrices.
        """
        for longitud_actual in range(1, n+1):
            for inicio in range(0, n-longitud_actual+1):
                fin = inicio + longitud_actual      
                """
                Almacenamos inicio a fin de w de la forma de la entrada de esa
                fila pero en el anterior elemeneto, mas la probabilidad de este elemento y su probabilidad de
                pseudo
                """
                
                self.w[inicio][fin] = (
                    self.w[inicio][fin-1] + self.p[fin-1] + self.pseudo[fin]
                )
                
                # Almacenamos la de e inicio a fin como infinito
                self.e[inicio][fin] = float("inf")

                """
                Igual que en multiplicacion de matrices, recorremos puntos medios desde el inicio+1 hata fin+1
                y calculamos su coste de la forma de:
                
                self.e[inicio][punto_medio-1]
                + self.e[punto_medio][fin]
                + self.w[inicio][fin]
                
                Y preguntamos si este nuevo valor es menor que el que teniamos, si lo es lo almacenamos este nuevamente
                y guardamos en la raiz el punto medio de este.
                """
                for punto_medio in range(inicio+1, fin+1):
                    coste = (
                        self.e[inicio][punto_medio-1] +          # coste subárbol izquierdo
                        self.e[punto_medio][fin]   +          # coste subárbol derecho
                        self.w[inicio][fin]              # peso total
                    )
                    if coste < self.e[inicio][fin]:
                        self.e[inicio][fin] = coste
                        self.raiz_[inicio][fin] = punto_medio      # guardamos la clave raíz óptima


    def __create_tree(self, from_=1, to_=None, root=None, altura = 0):


        """
        Si el destino del arbol pasado por parámetros es mayor que desde donde partimos
        retornamos None ya que no es posible fisicamente
        """
        if to_ is not None and from_ > to_:
            return None
        
        # Si no se ha indicado destino del arbol se hara hacia el ultimo nodo, es decir, la longitud del arbol
        if to_ is None:
            to_ = len(self.p)
        
        """
        Si el nodo padre es None, se instancia en vacio y se almacena en atributos publicos
        """
        if root is None:
            root = {}
            self.root = root          # atributo público con la raíz
        
        # Si la altura indicada es mayor que la altura de los atributos publicos se actualiza
        if altura > self.altura:
            self.altura = altura

        """
        I es el indice desde el que partimos, es decir, from - 1 y j hacia el que vamos j
        Una vez inicializados si el indice de inicio es superior o igual al de fin retornamos None
        """
        i = from_ - 1                 # 0-based
        j = to_                       # inclusive
        if i >= j:                    # subárbol vacío
            return None
        
        
        """
        r -> Raiz
        k -> clave
        v -> valor
        h -> altura
        coste -> coste
        
        Una vez tengamos todo almacenamos todos los valores 
        """
        r = self.raiz_[i][j]          # índice 1-based de la clave raíz
        root["k"] = self.claves[r-1]  # clave
        root["v"] = r                 # posición 1-based (para __search)
        root["h"] = altura
        root["coste"] = self.e[i][j]

        root["izq"] = self.__create_tree(from_, r-1, {}, altura+1)
        root["der"] = self.__create_tree(r+1, to_, {}, altura+1)
        return root
    
    def __search(self, clave=None):
        
        # Si no existe clave, devolvemos la raiz.
        if clave is None:
            return self.root
        
        """
        Si hay clave, la raiz es el padre y extraemos todos los valores numericos desde el segundo 
        elemento para evitar a la raiz hacia adelante
        """
        raiz = self.root
        value = int(clave[1:])
        
        """
        Hacemos un bucle infinito preguntando
        si la raiz es None retornamos None
        Si la clave es igual a la clave de la raiz, es decir, que es el mismo, retornamos la raiz
        """
        while True:
            if raiz is None:
                return None
            elif clave == raiz['k']:
                return raiz
            else: 
                """
                En caso contrario, si el valor es mayor que el valor de la raiz, devolvemos
                la raiz del de la derecha, si no del de la izquierda.
                """
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
        izq = self.__str__(raiz['izq']["k"]) if raiz['izq'] is not None else ""
        der = self.__str__(raiz['der']["k"]) if raiz['der'] is not None else ""
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

    def coste_esperado(self, clave=None):
        """
        Devuelve el coste esperado de la búsqueda en el subárbol asociado a una
        clave.
        Si clave es None, devuelve el coste del árbol completo.
        """
        return self.__search(clave)["coste"]
        
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
    
