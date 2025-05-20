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
        
        # Instanciamos la matriz de adyacencia y nodos intermedios
        matriz_adyacencia = {}  # Costes directos entre nodos
        matriz_intermedios = {}  # Nodos intermedios para reconstruir caminos

        # Construimos las matrices iniciales
        """
        Recorremos el origen y destino del grafo:
        si el origen no eta en la matriz de adyacencia, creamos una entrada vacia
        en la matriz de adyacencia y en la de intermedios de este nodo.
        Si el de destino no esta tampoco repetimos lo mismo.
        """
        for (origen, destino) in grafo:
            if origen not in matriz_adyacencia:
                matriz_adyacencia[origen] = {}
                matriz_intermedios[origen] = {}
            if destino not in matriz_adyacencia:
                matriz_adyacencia[destino] = {}
                matriz_intermedios[destino] = {}

            # Almacenamos el coste de origen y destino del grafo en la matriz de adyacencia
            matriz_adyacencia[origen][destino] = grafo[(origen, destino)]
            
            # En este momento aun no tenemos nodos intermedios, por lo que, 0
            matriz_intermedios[origen][destino] = 0

        """
        Inicializamos la matriz de distancias haciendo una copia profunda ya que si hacemos
        m = x hace una referencia y no es lo que necesitamos
        """
        matriz_distancias = copy.deepcopy(matriz_adyacencia)
        
        """
        Recorremos los nodos de la matriz de distancias y dentro esta nuevamente
        preguntamos si ambos nodos son igules, si lo son, la distancia es 0.
        Si el nodo 2 no esta en la matriz de distancias del nodo 1, la distancia
        como no hay camino, sera infinito
        """
        for nodo1 in matriz_distancias:
            for nodo2 in matriz_distancias:
                if nodo1 == nodo2:
                    matriz_distancias[nodo1][nodo2] = 0
                elif nodo2 not in matriz_distancias[nodo1]:
                    matriz_distancias[nodo1][nodo2] = float("inf")

        """
        Finalmente aplicamos el algoritmo de Floyd.
        
        Recorremos 3 bucles simultaneamente, intermedio, origen y destino.
        Comprobamos si la distancia de origen a destino es mayor que la distancia del origen al intermedio y del intermedio al destino, si es asi, modificamos la matriz
        de distancia con este valor y convertirmo el intermedio en el nuevo intermedio. 
        """
        for intermedio in matriz_adyacencia:
            for origen in matriz_adyacencia:
                for destino in matriz_adyacencia:
                    if matriz_distancias[origen][destino] > matriz_distancias[origen][intermedio] + matriz_distancias[intermedio][destino]:
                        matriz_distancias[origen][destino] = matriz_distancias[origen][intermedio] + matriz_distancias[intermedio][destino]
                        matriz_intermedios[origen][destino] = intermedio

        # Guardamos resultados
        self.D = matriz_distancias
        self.P = matriz_intermedios
        
    def distancia(self, origen, destino):
        """
        Devuelve la distancia del camino mínimo ente origen y destino.
        Si no hay camino devuelve None.
        """
        
        """
        Extraemos el valor de distancia de origen a destino, si este es diferente de
        infinito lo retornamos, si no, retornamos None ya que si es infinito
        no tiene una distancia finita.
        """
        distancia = self.D[origen][destino]
        return distancia if distancia!= float("inf") else None
        
    def camino(self, origen, destino):
        """
        Devuelve en una lista de nodos el camino mínimo entre origen y
        destino.
        Si no hay camino devuelve None.
        """
        
        # Si el nodo de origen a destino es el mismo, el camino es el mismo.
        if origen == destino:
            return[origen]
        
        """
        Mediante un try catch 
        """
        try:
            
            # Extraemos el nodo intermedio de ambos
            nodo_intermedio = self.P[origen][destino]
            
            """
            Si el nodo intermedio es 0 significa que no tiene nodo intermedio y que
            el camino, es directo y el camino minimo es origen a destino.
            """
            if nodo_intermedio == 0:
                return [origen, destino]
                
                """
                Si no es 0 significa que si tiene un camino con nodos intermedios.
                Calcula el camino desde origen hasta el intermedio, es decir, el camino de la izquierda
                y calculamos el camino desde el intermedio hasta el destino
                """
            else:
                camino_izquierda = self.camino(origen, nodo_intermedio)
                camino_derecha = self.camino(nodo_intermedio, destino)
                
                """
                Retornamos el camino de la izquierda sumado del camino de la derecha.
                Pero con la peculiaridad de que el camino de la derecha empezamos en el segundo
                ya que si no el intermedio estaría repetido en el camino de la izquierda 
                y en el camino de la derecha
                """
                return camino_izquierda + camino_derecha[1:]
            """
            Si lanza la excepción de KeyError es porque no existe esa combinación de origen y destino
            y por tanto antes de lanzar un error retornamos un None ya que no existe camino posible
            """
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
    
    """
    Instanciamos n que es el tamaño es el número de matrices, le restamos uno ya que recordemos que:
    M1 = x1 * x2
    M2 = x2 * x3
    M3 = x3 * x4

    Por lo que la dimensión es [x1,x2,x3,x4] y el numero de matrices es el número
    de dimensiones menos 1.
    
    Tambien instanciamos la tabla dinamica, que es de la forma de 
    [(0,"M_1"), (0,"M_2"),..., (0,"M_N"),
    (0,"M_1"), (0,"M_2"),..., (0,"M_N")]
    """
    n = len(dimensiones) - 1

    # Creamos la tabla dinámica con pares: (coste mínimo, expresión como string)
    tabla_dinamica = [[(0, f"M_{i}") for i in range(1, n + 1)] for _ in range(n)]

    # longitud_actual: número de matrices a multiplicar en esta iteración (2, 3, ..., n)
    for longitud_actual in range(2, n + 1):  # empieza en 2 porque ya tenemos los costes de una sola matriz
        for inicio in range(n - longitud_actual + 1):
            fin = inicio + longitud_actual - 1
            mejor_coste = float("inf")
            mejor_expresion = ""

            # punto_de_corte divide la cadena de matrices en dos partes: izquierda y derecha
            for punto_de_corte in range(inicio, fin):
                coste_izq, expr_izq = tabla_dinamica[inicio][punto_de_corte]
                coste_der, expr_der = tabla_dinamica[punto_de_corte + 1][fin]

                coste_total = coste_izq + coste_der + dimensiones[inicio] * dimensiones[punto_de_corte + 1] * dimensiones[fin + 1]

                if coste_total < mejor_coste:
                    mejor_coste = coste_total

                    # Solo se usan paréntesis si hay más de una matriz en la parte
                    if len(expr_izq) > 3:
                        expr_izq = f"({expr_izq})"
                    if len(expr_der) > 3:
                        expr_der = f"({expr_der})"

                    mejor_expresion = f"{expr_izq}*{expr_der}"

            tabla_dinamica[inicio][fin] = (mejor_coste, mejor_expresion)

    return tabla_dinamica[0][-1]



