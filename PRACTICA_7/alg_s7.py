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
    
    """
    Sencillamente preguna si es de un tipo u otro y lanza su función, si no es ninguna lanza un error.
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
    """
    Almacanemos como funcion la key_function ya que si es reverse convertimos los valores a negativos para hacerlo de mayor a menor
     
    """
    function = key_function
    if reverse:
        function = lambda x : -key_function(x)
    
    # Si la secuencia no tiene elementos o solo 1 la retornamos tal cual
    if len(sequencia) <= 1:
        return sequencia
    
    
    # Almacenamos el valor de la mitad dividiendo la secuencia entre dos y al hacer con el operador "//" solo almacenamos el valor entero
    mitad = len(sequencia) // 2
    
    """
    Con el valor de la mitad en enteros creamos dos listas:
    izquierda que sera desde el primer elemento hasta el valor de mitad y derecha
    que será desde el valor de la mitad hasta el final
    """
    izquierda = sequencia[:mitad]
    derecha = sequencia[mitad:]

    """
    Una vez con ambas listas se llamará a esta función de forma recursiva hasta que las listas solo tengan un elemento
    """
    izquierda = mergesort(izquierda, key_function,reverse)
    derecha = mergesort(derecha, key_function,reverse)
    
    # Llamamos a la función _merge en cada llamada 
    return _merge(izquierda, derecha, function)


def _merge(izquierda, derecha, key_function):
    
    # Convertimos las listas en interadores
    iter_izq = iter(izquierda)
    iter_der = iter(derecha)
    
    # Creamos la lista para almacenar el resultado
    resultado = []

    # Extraemos ahora el elemento de la izquierda y de la derecha, si no existe, se convierte en None.
    elem_izq = next(iter_izq, None)
    elem_der = next(iter_der, None)

    # Mientras el resultado sea menor que la suma de las longitudes de ambas listas se hará el bucle
    while len(resultado) < len(izquierda) + len(derecha):
        
        """
        Si el elemento de la izquierda es None se agrega el elemento de la derecha y se continua interando 
        pero en la iteración de la derecha
        """
        if elem_izq is None:
            resultado.append(elem_der)
            elem_der = next(iter_der, None)
            
        elif elem_der is None:
            """
            En caso contrario, si el que es None es el de la derecha, almacenamos el valor de la izquierda y avanzamos este valor
            Si ya no quedan mas será none
            """
            resultado.append(elem_izq)
            elem_izq = next(iter_izq, None)
        elif key_function(elem_izq) <= key_function(elem_der):
            """
            Los casos anteriores es si algun valor es None, una vez ya no sea None, hacemos uso de la key_function para comparar
            Si la función comparadora del elemento de la izquierda es menor o igual que el de la derecha, se agrega al resultado el elemento de la izquierda
            y se avanza el elemento de la izquierda (S no quedan más sera None) 
            """
            resultado.append(elem_izq)
            elem_izq = next(iter_izq, None)
        else:
            """
            Si la función comparadora sobre el elemento de la derecha es mayor, el que se agrega es el valor de la derecha y se avanza este.
            """
            resultado.append(elem_der)
            elem_der = next(iter_der, None)

    # Finalmente retornamos el resultado
    return resultado




def quicksort(sequencia, key_function, reverse):
    """
    Ordena la secuencia dada con el algoritmo quicksort.

    La secuencia puede ser una lista o una tupla.

    La función key_function se aplica a cada elemento de la secuencia para obtener el valor que se usará para comparar los elementos.

    Si reverse es True, el orden es descendente.

    Puedes utilizar el método de partición que quieras.

    """
    
    """
    Exactamente igual que el merge sort, creamos la funcion que sera la key function, si esta es reverse se convertira todos
    los valores de la key_function que retorna en negativos
    """
    function = key_function
    if reverse:
        function = lambda x : -key_function(x)
        
    # Finalmente retornamos la llamada a la función de quicksort
    return _quicksort(sequencia,function)

def _quicksort(sequencia,key_fuction):
    
    # Si la secuencia tiene uno o ningun elemento se retorna la secuencia.
    if len(sequencia)<=1:
        return sequencia
    
    # Selecciona el pivote como el primer elemento de la lista.
    pivote = sequencia[0]
    
    # Se crean las particiones pero sin el elemento pivote
    izquierda,derecha = _particion(sequencia[1:],pivote,key_fuction)
    
    """
    Creamos una salida que es la lista de la izquierda, el pivote y la lista de la derecha
    
    """
    return _quicksort(izquierda,key_fuction) + [pivote] + _quicksort(derecha,key_fuction)

def _particion(sequencia,pivote,key_function):
    
    # Creamos ambas listas vacias para almacenar los valores de ambas listas
    
    izquierda = []
    derecha = []
    
    """
    Recorremos los elementos de la secuencia y si el elemento es menor que el pivote por la funcion comparadora se guarda en la lista de la izquierda.
    En caso contrario se almacena en la lista de la derecha
    """
    for elem in sequencia:
        if key_function(elem) <= key_function(pivote):
            izquierda.append(elem)
        else:
            derecha.append(elem)
    
    # Una vez recorrido todos los elementos se almacenan se retornan ambas listas
    return izquierda, derecha

# Sugerencia: Prueba los tiempos de los distitnos algoritmos de ordenación, así como sus variantes.

# Sugerencia: Comprueba formalmente y experimentalmente los tiempos de ordenación de los algoritmos para conjuntos ya ordenados, conjuntos ordenados en orden inverso y conjuntos aleatorios.

# Sugerencia: Prueba los tiempos comparando tu implementación con la del Timsort incluida en la función sorted de Python.