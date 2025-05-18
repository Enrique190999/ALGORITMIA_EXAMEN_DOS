# # Algoritmia
# ## Práctica 9
# En esta práctica se resolverá el problema de Subsecuencia Común Más Larga (LCS) y el problema de la mochila 1-0.


# Subsecuencia Común Más Larga (LCS)

def es_subsecuencia(subsecuencia, secuencia):
    iterador = iter(secuencia)
    
    return all(caracter in iterador for caracter in subsecuencia)

def subsecuencia_comun_mas_larga(x, y):
    m = len(x)
    n = len(y)
    
    tabla_dp = [[""] * (n+1) for _  in range(m+1)]
    
    for i in range(n+1):
        for j in range(m+1):
            if x[i-1] == y[i-1]:
                tabla_dp[i][j] = tabla_dp[i-1][j-1] + x[i-1]
            else:
                tabla_dp[i][j] = max(tabla_dp[i-1][j], tabla_dp[i][j-1], key= len)
        
    return tabla_dp[m][n]


def subsecuencias_comunes_mas_largas(x, y):
    m = len(x)
    n = len(y)
    
    tabla_dp = [[set() for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(n+1):
        for j in range(m+1):
            if i== 0 or j==0:
                tabla_dp[i][j] = {""}
            elif x[i-1] == j[i-1]:
                tabla_dp[i][j] = {x[i-1] + s for s in tabla_dp[i-1][j-1]}
            else:
                tabla_dp[i][j] = tabla_dp[i-1][j] | tabla_dp[i][j-1]
            
            if len(next(iter(tabla_dp[i][j-1]),"")) > len(next(iter(tabla_dp[i-1][j]),"")):
                tabla_dp[i][j] = tabla_dp[i][j-1]
            elif len(next(iter(tabla_dp[i][j-1]),"")) < len(next(iter(tabla_dp[i-1][j]),"")):
                tabla_dp[i][j] = tabla_dp[i-1][j]
    
    max_length = max(len(s) for s in tabla_dp[m][n])
    return { s for s in tabla_dp[m][n] if len(s) == max_length}

def mochila(objetos, capacidad):
    pass