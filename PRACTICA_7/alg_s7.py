# # Algoritmia
# ## Práctica 7
# En esta práctica se resolverá el problema de ordenación Divide y Vencerás

# En el cuerpo de cada función o método a implementar hay una instrucción "pass", se debe sustituir por la implementación adecuada.

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.

# NO se deberá utilizar el método sort de las listas de Python. Se deberán implementar los algoritmos de ordenación.

def ordena(sequencia, key_function=lambda x:x, reverse=False, tipo="mergesort"):
    """
    Ordena la secuencia dada.

    La secuencia puede ser una lista o una tupla.

    La función key_function se aplica a cada elemento de la secuencia para obtener el valor que se usará para comparar los elementos.

    Si reverse es True, el orden es descendente.

    El parámetro tipo indica el algoritmo de ordenación a usar. Puede ser "mergesort" o "quicksort".
    """
    if tipo == "mergesort":
        return mergesort(sequencia, key_function, reverse)
    elif tipo == "quicksort":
        return quicksort(sequencia, key_function, reverse)
    else:
        raise ValueError("Tipo de ordenación no válido")
 

def mergesort(sequencia, key_function, reverse):
    """
    Ordena la secuencia dada con el algoritmo mergesort.

    La secuencia puede ser una lista o una tupla.

    La función key_function se aplica a cada elemento de la secuencia para obtener el valor que se usará para comparar los elementos.

    Si reverse es True, el orden es descendente.
    """
    function = key_function
    if reverse:
        function = lambda x : -key_function(x)
    if len(sequencia) <= 1:
        return sequencia
    
    mitad = len(sequencia) // 2
    izquierda = sequencia[:mitad]
    derecha = sequencia[mitad:]

    izquierda = mergesort(izquierda, key_function,reverse)
    derecha = mergesort(derecha, key_function,reverse)
    
    return _merge(izquierda, derecha, function)


def _merge(izquierda, derecha, key_function):
    iter_izq = iter(izquierda)
    iter_der = iter(derecha)
    res = []

    elem_izq = next(iter_izq, None)
    elem_der = next(iter_der, None)

    while len(res) < len(izquierda) + len(derecha):
        if elem_izq is None:
            res.append(elem_der)
            elem_der = next(iter_der, None)
        elif elem_der is None:
            res.append(elem_izq)
            elem_izq = next(iter_izq, None)
        elif key_function(elem_izq) <= key_function(elem_der):
            res.append(elem_izq)
            elem_izq = next(iter_izq, None)
        else:
            res.append(elem_der)
            elem_der = next(iter_der, None)

    return res




def quicksort(sequencia, key_function, reverse):
    """
    Ordena la secuencia dada con el algoritmo quicksort.

    La secuencia puede ser una lista o una tupla.

    La función key_function se aplica a cada elemento de la secuencia para obtener el valor que se usará para comparar los elementos.

    Si reverse es True, el orden es descendente.

    Puedes utilizar el método de partición que quieras.

    """
    function = key_function
    if reverse:
        function = lambda x : -key_function(x)
    return _quicksort(sequencia,function)

def _quicksort(sequencia,key_fuction):
    if len(sequencia)<=1:
        return sequencia
    pivote = sequencia[0]
    izquierda,derecha = _particion(sequencia[1:],pivote,key_fuction)
    return _quicksort(izquierda,key_fuction) + [pivote] + _quicksort(derecha,key_fuction)

def _particion(sequencia,pivote,key_function):
    izquierda = []
    derecha = []
    for elem in sequencia:
        if key_function(elem) <= key_function(pivote):
            izquierda.append(elem)
        else:
            derecha.append(elem)
    return izquierda, derecha

# Sugerencia: Prueba los tiempos de los distitnos algoritmos de ordenación, así como sus variantes.

# Sugerencia: Comprueba formalmente y experimentalmente los tiempos de ordenación de los algoritmos para conjuntos ya ordenados, conjuntos ordenados en orden inverso y conjuntos aleatorios.

# Sugerencia: Prueba los tiempos comparando tu implementación con la del Timsort incluida en la función sorted de Python.