# # Algoritmia
# ## Práctica 7
# En esta práctica se resolverá el problema de subvector de suma máxima.

# Definición del problema:
# - Se tiene un vector de números, positivos y negativos.
# - Se debe encontrar el valor máximo que se puede obtener sumando los elementos de un subvector contiguo del vector dado.
# # Aproximación por fuerza bruta:
# # - Se consideran todos los subvectores posibles.
# # - Se calcula la suma de cada uno de ellos.
# # - Se devuelve la mayor suma obtenida.
# # Aproximación Divide y Vencerás:
# # - Se divide el vector en dos mitades.
# # - Se calcula la suma máxima de un subvector que está en la primera mitad.
# # - Se calcula la suma máxima de un subvector que está en la segunda mitad.
# # - Se calcula la suma máxima de un subvector que pasa por el medio.
# # - Se devuelve la mayor de las tres sumas anteriores.
# # - La suma máxima de un subvector que pasa por el medio se calcula sumando los elementos desde la mitad hacia la izquierda y desde la mitad hacia la derecha.

# En el cuerpo de cada función o método a implementar hay una instrucción "pass", se debe sustituir por la implementación adecuada.

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.


def subvector_suma_maxima_fuerza_bruta(vector):
    """
    Devuelve la suma máxima de un subvector contiguo del vector dado.
    Aproximación por fuerza bruta.
    """
    
    # Inicializamos el máximo de la suma en -infinito
    max_suma = float('-inf')
    
    # El máximo de elementos será la longitud del vector
    n = len(vector)
    
    """
    Recorremos el vector desde 0 hasta n
    luego desde el indice que estemos recorremos hasta n
    Dentro de ello haremos un sumatorio desde el inicio hasta el final + 1 y el maximo actual será
    el maximo entre el que habia y el actual
    [1-8]
    Primera suma [1-2]
    Segunda suma [1-3]
    ....
    """
    for inicio in range(n):
        for final in range(inicio, n):
             suma_subvector = sum(vector[inicio:final+1])
             max_suma = max(max_suma,suma_subvector)
    
    # Finalmente retornamos la suma
    return max_suma

def subvector_suma_maxima_divide_y_venceras(vector):
    """
    Devuelve la suma máxima de un subvector contiguo del vector dado.
    
    Aproximación Divide y Vencerás.
    """
    return suma_maxima(vector, 0, len(vector) - 1)

def suma_maxima(vector, izquierda, derecha):

    if izquierda == derecha:
        return vector[izquierda]

    medio = (izquierda + derecha) // 2

    max_izquierda = suma_maxima(vector, izquierda, medio)
    max_derecha = suma_maxima(vector, medio + 1, derecha)

    # Suma máxima cruzando el medio
    suma_izquierda = float('-inf')
    suma_actual = 0
    for i in range(medio, izquierda - 1, -1):
        suma_actual += vector[i]
        suma_izquierda = max(suma_izquierda, suma_actual)

    suma_derecha = float('-inf')
    suma_actual = 0
    for i in range(medio + 1, derecha + 1):
        suma_actual += vector[i]
        suma_derecha = max(suma_derecha, suma_actual)

    suma_central = suma_izquierda + suma_derecha

    return max(max_izquierda, max_derecha, suma_central)
# Sugerencia: analiza el tiempo de ejecución de cada una de las funciones anteriores.

# Sugerencia: crea una versión de estos algoritmos que además devuelva los índices del subvector de suma máxima.