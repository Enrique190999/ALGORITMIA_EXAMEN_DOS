# # Algoritmia
# ## Práctica 9
# En esta práctica se resolverá el problema de Subsecuencia Común Más Larga (LCS) y el problema de la mochila 1-0.


# Subsecuencia Común Más Larga (LCS)

def es_subsecuencia(subsecuencia, secuencia):
    """Indica si el primer argumento es subsecuencia del segundo"""
    
    # Convertimos la secuencia en un iterador
    iterador = iter(secuencia)
    
    """
    Esta linea comprueba que caractera a caracter del iterador este en la subsecuencia.
    El all hace que cada iteracion ([True,True,True]) = True se compruebe que todos los elementos
    del iterable sean True, si no False
    """
    return all(caracter in iterador for caracter in subsecuencia)


def subsecuencia_comun_mas_larga(x, y):
    """
    Dadas dos cadenas x e y devuelve una que es subsecuencia de ambas y que 
    tiene la longitud máxima de todas las subsecuencias comunes.
    """
    
    # Almacenamos las longitudes de ambas subsecuencias
    m = len(x)
    n = len(y)
    
    # Crear una tabla para almacenar las longitudes de las subsecuencias comunes
    tabla_dp = [[""] * (n + 1) for _ in range(m + 1)]
    
    """
    Recorremos la tabla de (m+1)(n+1)
    """
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            
            # Si de ambas cadenas coinciden el caracter reescribo la tabla
            if x[i - 1] == y[j - 1]:
                
                # Agrego el caracter a la subsecuencia que extraje en la anterior iteración
                tabla_dp[i][j] = tabla_dp[i - 1][j - 1] + x[i - 1]
            else:
                
                # Si no son iguales seleccionamos la que sea mas larga de arriba o de la izquierda
                tabla_dp[i][j] = max(tabla_dp[i - 1][j], tabla_dp[i][j - 1], key=len)
    
    # Finalmente retornamos la tabla en su ultima posición 
    return tabla_dp[m][n]
    # TRUCO VISUAL: Se instancia en orden de x,y pero en orden de m,n y la tabla se hace de n*m y se recorre y se retorna de m*n.

def subsecuencias_comunes_mas_largas_profesor(x,y):
    """
    Dadas dos cadenas x e y devuelve una que es subsecuencia de ambas y que 
    tiene la longitud máxima de todas las subsecuencias comunes.
    """
    
    # Almacenamos las longitudes de ambas subsecuencias
    m = len(x)
    n = len(y)
    
    # Crear una tabla para almacenar las longitudes de las subsecuencias comunes
    tabla_dp = [[""] * (n + 1) for _ in range(m + 1)]
    
    """
    Recorremos la tabla de (m+1)(n+1)
    """
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            
            # Si de ambas cadenas coinciden el caracter reescribo la tabla
            if x[i - 1] == y[j - 1]:
                
                # Agrego el caracter a la subsecuencia que extraje en la anterior iteración
                tabla_dp[i][j] = tabla_dp[i - 1][j - 1] + x[i - 1]
            else:
                
                # Si no son iguales seleccionamos la que sea mas larga de arriba o de la izquierda
                tabla_dp[i][j] = max(tabla_dp[i - 1][j], tabla_dp[i][j - 1], key=len)
    
    # Creamos una funcion para construir todas las subsecuencias comunes mas larga
    def subsecuencia_comun_mas_larga(fila,columna) -> set:
        
        # Si ya no quedan mas caracteres retornamos en blanco y finalizamos
        if fila == 0 or columna == 0:
            return {" "}
        
        """
        Si son el mimso elemento en diagonal retornamos
        el caracter actual mas los caracteres de la anterior subsecuencia
        """
        if x[fila-1][columna] == y[fila][columna - 1]:
            return { x[fila-1] + s for s in tabla_dp[fila - 1][columna - 1]}
        
        """
        Si el de encima es mayor que el de la izquierda retornamos este, 
        si no el otro
        """
        if tabla_dp[fila - 1][columna] > tabla_dp[fila][columna - 1]:
            return subsecuencia_comun_mas_larga(fila-1,columna)
        elif tabla_dp[fila - 1][columna] < tabla_dp[fila][columna - 1]:
            return subsecuencia_comun_mas_larga(fila,columna - 1)
        
        """
        Si no se ha cumplido ninguna condicion retornamos la union de ambos subconjuntos
        
        """
        return subsecuencia_comun_mas_larga(fila - 1,columna) | subsecuencia_comun_mas_larga(fila,columna - 1)

    
    return subsecuencia_comun_mas_larga(m,n)
    

def subsecuencias_comunes_mas_largas(x, y):
    """
    Dadas dos cadenas x e y devuelve un conjunto con todas las subsecuencias de 
    ambas que tienen longitud máxima.
    """
    
    # Almacenamos las longitudes de ambas subsecuencias
    m = len(x)
    n = len(y)
    
    # Crear una tabla para almacenar las longitudes de las subsecuencias comunes
    tabla_dp = [[set() for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Llenar la tabla dp
    # Recorremos la tabla entera, hasta aqui es igual que en la funcion pero en singular
    for i in range(m + 1):
        for j in range(n + 1):
            
            # Si es la primera posición se deja en blanco
            if i == 0 or j == 0:
                tabla_dp[i][j] = {""}
                
            # En caso contrario si los caracteres de ambas tablas son iguales
            elif x[i - 1] == y[j - 1]:
                
                """
                Si son caracteres iguales (DIFERENCIA CON LA DE SINGULAR)
                almacenamos en la tabla en la posición
                pero con la peculiaridad de recorrer todos los caracteres de la tabla de la posición anterior y agregandoles el caracter 
                que ha hecho coincidencia en esta iteración pero en la posición de esta iteración
                """
                tabla_dp[i][j] = {s + x[i - 1] for s in tabla_dp[i - 1][j - 1]}
            else:
                
                """
                Si no hay coincidencia hace una unión, es decir, ejemplo:
                { "A", "AB" } | { "AC" } = { "A", "AB", "AC" }
                Junta en uno ambos conjuntos
                """
                tabla_dp[i][j] = tabla_dp[i - 1][j] | tabla_dp[i][j - 1]
                
                """
                Si la longitud del siguiente valor como iterador del de arriba es mayor que el de la izquierda almacenamos en la tabla el valor de arriba
                """
                if len(next(iter(tabla_dp[i - 1][j]), "")) > len(next(iter(tabla_dp[i][j - 1]), "")):
                    tabla_dp[i][j] = tabla_dp[i - 1][j]
                    
                # En caso contrario, almacenamos el de la izquierda
                elif len(next(iter(tabla_dp[i - 1][j]), "")) < len(next(iter(tabla_dp[i][j - 1]), "")):
                    tabla_dp[i][j] = tabla_dp[i][j - 1]
    
    """
    Una vez finalizado, se almacena la longitud mas larga de subsecuencia que se tenga
    y retornamos un conunto de todos las subsecuencias que tenga esa longitud
    """
    max_length = max(len(s) for s in tabla_dp[m][n])
    return {s for s in tabla_dp[m][n] if len(s) == max_length}

# Mochila 1-0

def mochila(objetos, capacidad):
    """
    Dada una capacidad y una lista de pesos y valores de n elementos, 
    devuelve el valor máximo que se puede obtener sin superar la capacidad y los objetos que se deben llevar.

    Los objetos no se pueden partir.
    """
    
    """
    Creamos la tabla donde cada entrada tendra una tupla de tipo (capacidad,[elementos]) 
    donde habrá una fila por cada capacidad, tambien cuenta la capacidad 0, por ello es range de capacidad mas uno
    """
    tabla = [(0, []) for _ in range(capacidad +1)]
    
    # Recorremos el indice y el peso y valor de los objetos
    for i, (peso,valor) in enumerate(objetos):
        
        """
        Hacemos otro bucle donde recorremos desde la capacidad, hasta el menor peso, con paso de -1, es decir,
        de atras hacia alante
        """
        for j in range(capacidad, peso -1,-1):
            
            """Si la capacidad de la entrda de la fila de donde estamos restando el peso para la posición 
            y sumando su valor es mayor que el que queremos introducir ahora, introduciremos 
            """
            if tabla[j-peso][0] + valor > tabla[j][0]:
                tabla[j] = (tabla[j-peso][0] +valor ,[i] +tabla[j-peso][1])
    return tabla[capacidad]


# Sugerencia: Haz la función mochila con complejidad espacial O(W)