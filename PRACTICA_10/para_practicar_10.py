# # Algoritmia
# ## Práctica 10
# En esta práctica se resolverá el problema de los caminos mínimos entre todos los nodos de un grafo.
# Y la multiplicación de matrices.
 
import copy

class CaminosMinimosFloyd:

    def __init__(self, grafo):
        matriz_adyacencia = {}
        matriz_intermedios = {}
        
        for (origen,destino) in grafo:
            if origen not in matriz_adyacencia:
                matriz_adyacencia[origen] = {}
                matriz_intermedios[origen] = {}
            elif destino not in matriz_adyacencia:
                matriz_adyacencia[destino] = {}
                matriz_intermedios[destino] = {}

            matriz_distancias[origen][destino] = grafo[(origen,destino)]
            matriz_intermedios[origen][destino] = 0
            
        import copy
        matriz_distancias = copy.deepcopy(matriz_adyacencia)
        
        for nodo1 in matriz_distancias:
            for nodo2 in matriz_distancias:
                if nodo1 == nodo2:
                    matriz_distancias[origen][destino] = 0
                elif nodo2 not in matriz_distancias[nodo1]:
                    matriz_distancias[nodo1][nodo2] = float('inf')
        
        for intermedio in matriz_distancias:
            for origen in matriz_distancias:
                for destino in matriz_distancias:
                    coste_calculado = matriz_distancias[origen][intermedio] + matriz_distancias[intermedio][fin]
                    if coste_calculado < matriz_distancias[origen][destino]:
                        matriz_distancias[origen][destino] = coste_calculado
                        matriz_intermedios[origen][destino] = intermedio
        
        self.D = matriz_distancias
        self.P = matriz_intermedios
        pass      
    
    def distancia(self, origen, destino):
        distancia = self.D[origen][destino]
        
        return distancia if distancia != float('inf') else None
        pass
        
    def camino(self, origen, destino):
        if origen == destino:
            return[origen]
        try:
            intermedio = self.P[origen][destino]
            
            if intermedio == 0:
                return [origen,destino]
            else:
                izq = self.camino(origen,intermedio)
                der = self.camino(intermedio,destino)
                
                return [izq] + [der[1:]]
            pass
        except KeyError:
            return None
        pass

def multiplicacion_encadenada_matrices(dimensiones):
    pass
    n = len(dimensiones) - 1
    tabla = [[(0,f"M_{i}") for i in range(1,n+1)] for _ in range(n)]
    
    for long_actual in range(2,n+1):
        for inicio in range(n-long_actual + 1):
            fin = inicio + long_actual - 1
            mejor_expr = ""
            mejor_coste = float('inf')
            
            for punto_medio in range(inicio,fin):
                mejor_izq,exp_izq = tabla[inicio, punto_medio]
                mejor_der,exp_der = tabla[punto_medio + 1,fin]
                coste_total = (
                    mejor_der + 
                    mejor_izq + 
                    (dimensiones[inicio] * dimensiones[punto_medio - 1] * dimensiones[fin - 1])
                )
                
                if coste_total < tabla[inicio][fin]:
                    mejor_coste = coste_total
                    
                    if len(exp_der) > 3:
                        exp_der = f"({exp_der})"
                    
                    if len(exp_izq) > 3:
                        exp_izq = f"({exp_izq})"
                    mejor_expr = f"({exp_der}*{exp_izq})"
                
                tabla[inicio][fin] = (mejor_coste,mejor_expr)
    return tabla[0][-1]