# # Algoritmia
# ## Práctica 10
# En esta práctica se resolverá el problema de los caminos mínimos entre todos los nodos de un grafo.
# Y la multiplicación de matrices.
 
import copy


class CaminosMinimosFloyd:
    """
    Clase para representar los caminos mínimos entre todos los nodos de un grafo.
    Los caminos deben calcularse con el algoritmo de Floyd.
    El espacio de almacenamiento debe ser O(n^2), siendo n el número de nodos.
    """

    def __init__(self, grafo):
        """
        Constructor que recibe el grafo sobre el que calcular los caminos
        mínimos.
        El grafo que se recibe es un diccionario donde las claves son arcos 
        (pares de nodos) y los valores son el peso de los arcos.
        """
        G = {}
        P = {}
        for g in grafo:
            f, t = g
            if f not in G:
                G[f] = {}
                P[f] = {}
            if t not in G:
                G[t] = {}
                P[t] = {}

            G[f][t] = grafo[g]
            P[f][t] = 0

        D = copy.deepcopy(G)  # Complejidad N^2
        for i in D:
            for j in D:
                if i == j:
                    D[i][j] = 0  
                elif j not in D[i]:
                    D[i][j] = float("inf")  

        for k in G:
            for i in G:
                for j in G:
                    if D[i][j] > D[i][k] + D[k][j]:
                        D[i][j] = D[i][k] + D[k][j]
                        P[i][j] = k

        self.D = D
        self.P = P
    def distancia(self, origen, destino):
        """
        Devuelve la distancia del camino mínimo ente origen y destino.
        Si no hay camino devuelve None.
        """
        d = self.D[origen][destino]
        return d if d!= float("inf") else None
        
    def camino(self, origen, destino):
        """
        Devuelve en una lista de nodos el camino mínimo entre origen y
        destino.
        Si no hay camino devuelve None.
        """
        if origen == destino:
            return[origen]
        try:
            k = self.P[origen][destino]
            if k == 0:
                return [origen, destino]
            else:
                subpath_izq = self.camino(origen, k)
                subpath_der = self.camino(k, destino)
                return subpath_izq +subpath_der[1:]
        except KeyError:
            return None


def multiplicacion_encadenada_matrices(dimensiones):
    """
    Dadas las dimensiones de varias matrices a multiplicar, aplica el método
    de programación dinámica para para determinar en qué orden realizar las
    multiplicaciones.
    El número de matrices será la longitud de dimensiones menos uno.
    Las dimensiones de la matriz M_i están en las componentes i-1 e i de
    'dimensiones'.
    Devuelve el número de multiplicaciones de elementos a realizar y una
    cadena con la fórmula, incluyendo paréntesis (solo si son necesarios), en
    la que se realizarían las multiplicaciones.
    Por ejemplo '(M_1*(M_2*M_3))*M_4'.
    """
    n = len(dimensiones)-1
    m = [[(0,f"M_{i}") for i in range(1,n+1)] for j in range(n)]

    for d in range(1,n+1):
        for i in range(1, n-d+1):
            j = i +d
            max_ = float("inf")
            mult = ""
            for k in range(i,j):
                candidate = m[i-1][k-1][0] + m[k][j-1][0] + dimensiones[i-1] * dimensiones[k]*dimensiones[j]
                if candidate < max_:
                    max_ = candidate
                    left = m[i-1][k-1][1] if len(m[i-1] [k-1][1]) == 3 else f"({m[i-1][k-1][1]})"
                    right = m[k][j-1][1] if len(m[k] [j-1][1]) == 3 else f"({m[k][j-1][1]})"
                    mult = f"{left}*{right}"
            m[i-1][j-1] = (max_, mult)
    return m[0][-1]



