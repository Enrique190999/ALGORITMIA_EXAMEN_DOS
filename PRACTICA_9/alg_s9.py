# # Algoritmia
# ## Práctica 9
# En esta práctica se resolverá el problema de Subsecuencia Común Más Larga (LCS) y el problema de la mochila 1-0.


# Subsecuencia Común Más Larga (LCS)

def es_subsecuencia(subsecuencia, secuencia):
    """Indica si el primer argumento es subsecuencia del segundo"""
    it = iter(secuencia)
    return all(c in it for c in subsecuencia)


def subsecuencia_comun_mas_larga(x, y):
    """
    Dadas dos cadenas x e y devuelve una que es subsecuencia de ambas y que 
    tiene la longitud máxima de todas las subsecuencias comunes.
    """
    
    m, n = len(x), len(y)
    # Crear una tabla para almacenar las longitudes de las subsecuencias comunes
    dp = [[""] * (n + 1) for _ in range(m + 1)]
    # Llenar la tabla dp
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + x[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
    return dp[m][n]

def subsecuencias_comunes_mas_largas(x, y):
    """
    Dadas dos cadenas x e y devuelve un conjunto con todas las subsecuencias de 
    ambas que tienen longitud máxima.
    """
    
    m, n = len(x), len(y)
    # Crear una tabla para almacenar las longitudes de las subsecuencias comunes
    dp = [[set() for _ in range(n + 1)] for _ in range(m + 1)]
    # Llenar la tabla dp
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = {""}
            elif x[i - 1] == y[j - 1]:
                dp[i][j] = {s + x[i - 1] for s in dp[i - 1][j - 1]}
            else:
                dp[i][j] = dp[i - 1][j] | dp[i][j - 1]
                if len(next(iter(dp[i - 1][j]), "")) > len(next(iter(dp[i][j - 1]), "")):
                    dp[i][j] = dp[i - 1][j]
                elif len(next(iter(dp[i - 1][j]), "")) < len(next(iter(dp[i][j - 1]), "")):
                    dp[i][j] = dp[i][j - 1]

    max_length = max(len(s) for s in dp[m][n])
    return {s for s in dp[m][n] if len(s) == max_length}

# Mochila 1-0

def mochila(objetos, capacidad):
    """
    Dada una capacidad y una lista de pesos y valores de n elementos, 
    devuelve el valor máximo que se puede obtener sin superar la capacidad y los objetos que se deben llevar.

    Los objetos no se pueden partir.
    """
    
    tabla = [(0, []) for _ in range(capacidad +1)]
    for i, (peso,valor) in enumerate(objetos):
        for j in range(capacidad, peso -1,-1):
            if tabla[j-peso][0] + valor > tabla[j][0]:
                tabla[j] = (tabla[j-peso][0] +valor ,[i] +tabla[j-peso][1])
    return tabla[capacidad]


# Sugerencia: Haz la función mochila con complejidad espacial O(W)