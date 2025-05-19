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
        Recorremos la matriz de adyacencia 3 veces, del que sacamos intermedio, origen y destino
        y comprobamos si el coste de origen a destino es mayor que de origen a intermedio
        si lo es almacenamos el coste de origen a destino como el de origen a intermedio
        y en en la matriz de nodos intermedio de origen a destino introducimos este intermedio.
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
        d = self.D[origen][destino]
        return d if d!= float("inf") else None
        
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
    
    """
    Se instancia la tabla dinamica de la forma de (0,"M_i") tantas veces como n+1 y esto
    n veces.
    """
    tabla_dinamica = [[(0,f"M_{i}") for i in range(1,n+1)] for _ in range(n)]


    """
    Recorremos las longitudes de 1 a n+1
    Luego en el inicio de 1 hasta el numero de dimensiones menos la longitud mas 1
    
    La variable longitud indica cuantas matrices se van a multiplicar en esta iteración.
    
    Para ver la matriz en la que empezamos al número de matrices le restamos la longitud actual y le sumamos 1 para que el ultimo nodo se quede
    comprendido en el rango, ya que al hacer hasta longitud el ultimo no lo cuenta ya que internamente el indice es < x
    """
    for longitud in range(1,n+1):
        for inicio in range(1, n-longitud+1):
            
            # Calculamso el fin que es sumando el inicio y la longitud
            fin = inicio + longitud
            """
            Instanciamos temporalmente la variable max que contiene el valor maximo de la multiplicacion.
            mult contiene la multiplicación pero de forma de cadena de texto mediante el formateo en python
            """
            max_ = float("inf")
            mult = ""
            for k in range(inicio,fin):
                """
                El candidato se calcula sumando de la tabla dinamica:
                - inicio-1 k-1 y la posicion cero haciendo referencia al valor que quermos sumar.
                - k y fin - 1 
                - dimensiones [inicio - 1] * dimensiones[k] * dimensiones[fin]
                """
                
                candidato = tabla_dinamica[inicio-1][k-1][0] + tabla_dinamica[k][fin-1][0] + dimensiones[inicio-1] * dimensiones[k] * dimensiones[fin]
                
                """
                Si el candidato es mayor que el valor maximo que teniamos anteriormente.
                maximo ahora es el candidato.
                """
                if candidato < max_:
                    max_ = candidato
                    
                    # Obtenemos la expresión óptima del lado izquierdo (de M_inicio hasta M_k)
                    # Si su longitud es 3 (por ejemplo: "M_1"), significa que es una sola matriz y no necesita paréntesis
                    # En caso contrario (ya hay una multiplicación dentro), se envuelve entre paréntesis para respetar el orden
                    izquierda = tabla_dinamica[inicio - 1][k - 1][1] \
                        if len(tabla_dinamica[inicio - 1][k - 1][1]) == 3 \
                        else f"({tabla_dinamica[inicio - 1][k - 1][1]})"

                    # Hacemos lo mismo con la subexpresión derecha (de M_{k+1} hasta M_fin)
                    # Si es una matriz sola, se deja sin paréntesis; si no, se encapsula
                    derecha = tabla_dinamica[k][fin - 1][1] \
                        if len(tabla_dinamica[k][fin - 1][1]) == 3 \
                        else f"({tabla_dinamica[k][fin - 1][1]})"

                    # Unimos las dos subexpresiones con el símbolo de multiplicación
                    # Esta será la mejor forma encontrada hasta ahora de multiplicar de M_inicio a M_fin
                    mult = f"{izquierda}*{derecha}"

            # Finalmente en la tabla de inicio-1 y fin-1 almacenamos estos valores
            tabla_dinamica[inicio-1][fin-1] = (max_, mult)
            
            # Retornamos el valor del ultimo elemento de la ultima columna
    return tabla_dinamica[0][-1]



