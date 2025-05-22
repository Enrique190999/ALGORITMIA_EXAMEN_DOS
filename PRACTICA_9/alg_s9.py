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


def subsecuencias_comunes_mas_largas(x,y):
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
    def _subsecuencia_comun_mas_larga(fila,columna) -> set:
        
        # Si ya no quedan mas caracteres retornamos en blanco y finalizamos
        if fila == 0 or columna == 0:
            return {""}
        
        """
        Si son el mismo elemento en diagonal retornamos
        el caracter actual mas los caracteres de la anterior subsecuencia
        """
        if x[fila-1] == y[columna - 1]:
            return { s + x[fila-1] for s in _subsecuencia_comun_mas_larga(fila - 1,columna - 1)}
        
        """
        Si el de encima es mayor que el de la izquierda retornamos este, 
        si no el otro
        """
        if len(tabla_dp[fila - 1][columna]) > len(tabla_dp[fila][columna - 1]):
            return _subsecuencia_comun_mas_larga(fila-1,columna)
        elif len(tabla_dp[fila - 1][columna]) < len(tabla_dp[fila][columna - 1]):
            return _subsecuencia_comun_mas_larga(fila,columna - 1)
        """
        Si no se ha cumplido ninguna condicion retornamos la union de ambos subconjuntos
        
        """
        return _subsecuencia_comun_mas_larga(fila - 1,columna) | _subsecuencia_comun_mas_larga(fila,columna - 1)

    
    return _subsecuencia_comun_mas_larga(m,n)


def subsecuencia_comun_mas_larga(x, y):
    """
    Dadas dos cadenas x e y devuelve una que es subsecuencia de ambas y que 
    tiene la longitud máxima de todas las subsecuencias comunes.
    """
    
    # Almacenamos las longitudes de ambas cadenas
    m = len(x)
    n = len(y)
    
    # Crear una tabla para almacenar las longitudes de las subsecuencias comunes
    tabla_dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    """
    Rellenamos la tabla de dimensiones (m+1)x(n+1)
    donde cada celda contiene la longitud de la subsecuencia común más larga
    hasta ese punto.
    """
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Si los caracteres actuales coinciden, aumentamos la longitud
            if x[i - 1] == y[j - 1]:
                tabla_dp[i][j] = tabla_dp[i - 1][j - 1] + 1
            else:
                # Si no coinciden, tomamos la subsecuencia más larga hasta ahora
                tabla_dp[i][j] = max(tabla_dp[i - 1][j], tabla_dp[i][j - 1])
    
    # Reconstruimos una subsecuencia común más larga recorriendo la tabla desde el final
    fila, columna = m, n
    subsecuencia = []
    
    while fila > 0 and columna > 0:
        if x[fila - 1] == y[columna - 1]:
            # Si los caracteres coinciden, los añadimos a la solución
            subsecuencia.append(x[fila - 1])
            fila -= 1
            columna -= 1
        elif tabla_dp[fila - 1][columna] >= tabla_dp[fila][columna - 1]:
            fila -= 1
        else:
            columna -= 1
    
    # Invertimos la subsecuencia construida porque la hicimos hacia atrás
    return ''.join(reversed(subsecuencia))


# Mochila 1-0 O(w)

def mochila_ow(objetos, capacidad):
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

# Mochila o(n*w)
def mochila(objetos,capacidad):
    
    """
    Creamos la tabla que tendra una fila por cada objeto 
    (objetos + 1 para que cuente todos ellos)
    y dentro de cada fila habra una tupla con un valor númerico correpondiente
    a cada capacidad
    """
    tabla = [[(0) for _ in range(capacidad + 1)] for _ in range (len(objetos)+ 1)]
    
    # Recorremos este bucle por los objetos
    for i in range(1,len(objetos) + 1):
        
        # Recorremos este bucle por las capacidades
        for j in range(1,capacidad + 1):
            
            # Extraemos el objeto su peso y valor
            peso,valor = objetos[i-1]
            
            # Si el peso es mayor que la capacidad en la que estamos guardamos el elemento anterior
            if peso > j: 
                tabla[i][j] = tabla[i-1][j]
            else:
                
                # Si realmente este nuevo objeto entra sumamos el valor anterior el actual
                valor_mas_objeto  = tabla[i-1][j-peso] + valor
                
                if valor_mas_objeto > tabla[i-1][j]:
                    
                    # Si el valor a introducir es mayor que el anterior lo modificamos
                    tabla[i][j] = valor_mas_objeto
                
                else:
                    
                    # Si es mayor el que teniamos antes, guardamos el anterior
                    tabla[i][j] = tabla[i-1][j]
        
        # Ahora preparamos la salida
        objetos_retorno = []
        
        # Creamos dos índices, i para los objetos y j para la capacidad
        i = len(objetos)
        j = capacidad
        
        while i > 0 and j > 0:
            if tabla[i][j] != tabla[i-1][j]:
                objetos_retorno.append(i-1)
                j -= objetos[i-1][0]
            i -= 1
        
    return tabla[-1][-1], objetos_retorno
                
    

# Sugerencia: Haz la función mochila con complejidad espacial O(W)