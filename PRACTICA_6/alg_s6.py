# # Algoritmia
# ## Práctica 6
# En esta práctica se resolverá el problema de las Torres de Hanoi, con dos añadidos: el número de postes puede ser mayor que 3, los discos pueden estar en cualquiera de los postes.

# En el cuerpo de cada función o método a implementar hay una instrucción "pass", se debe sustituir por la implementación adecuada.

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.

class Hanoi:
    """Clase para representar las torres de Hanoi."""

    def __init__(self, discos, num_postes=None):
        """
        El parámetro discos es un entero o una secuencia.
        Si es un entero se refiere al número de discos en el primer poste.
        Si es una secuencia, cada elemento indica en qué poste está el disco.
        Los postes se identifican como 1, 2, 3...
        El primer elemento de la secuencia se refiere al disco más pequeño,
        el último al más grande.
        El parámetro num_postes es el número de postes.
        Si num_postes es None, será el máximo de 3 y el mayor valor que aparezca
        en discos
        """

        '''
        Comprobamos que la variable discos sea un numero, si es asi convertimos de un 
        numero entero a una colección de "1" igual al numero que tenia anteriormente.
        
        Si ya es una secuencia, se convierte a lista para asegurarnos que es modificable
        
        - Si le pasa un número habrá 3 discos y estaran todos en el poste 1.
        - Si le pasan una lista la posición de la lista representa el tamaño del disco
          si esto es [1,2,1] significa que en el poste 1 tenemos el disco 1 y 3 y en el poste 2
          el disco 2
        
        Si es número significa que habrá tantos discos como la cantidad de ese número
        en el primer poste.
        
        Es decir, si le pasamos un 8 posteriormente se convierte en [1,1,1,1,1,1,1,1] indicando
        que los 8 discos se encuentran en el poste 1.
        '''
        
        if isinstance(discos, int):
            discos = [1] * discos 
        else:
            discos = list(discos)
            
        # La almacenamos en la variable _discos del constructor
        self._discos = discos
        
        '''
        Si no se ha indicado numero de postes, por defecto seran desde
        3 hasta el valor más alto de la variable discos
        
        haremos un maximo de mínimo 3 hasta el número más alto de poste que se encuentre
        un disco en el.
        '''
        if num_postes is None:
            num_postes = max(3, max(discos))
        
        # Almacenamos el número de postes indicado por parámetros en nuestra variable del constructor.
        self._num_postes = num_postes

        '''
        La variable _postes del constructor se convertira en una matriz multidimensional que tendrá
        tantas filas como número de postes tengamos
        '''
        self._postes = [[] for _ in range(num_postes)]
        
        # Almacenamos la longitud de los discos
        longitud_discos = len(discos)
        
        # Recorremos del más grande al más pequeño [::-1] es el paso y significa lista invertida
        for disco in discos[::-1]:
            
            self._postes[disco - 1].append(longitud_discos)
            longitud_discos -= 1

    def __len__(self):
        """Devuelve el número de discos"""
        return len(self._discos)

    def __str__(self):
        return str(self._discos)

    def mueve(self, origen, destino):
        """Mueve el disco superior del poste origen al poste destino."""
        
        # Comprueba que el origen y el destino sea mayor o igual que 1 y menor o igual que el número de postes
        assert 1 <= origen <= self._num_postes
        assert 1 <= destino <= self._num_postes

        # Esto es ya que origen y destino es un numero desde 1 hasta n y las listas comienzan en 0, por ende, se resta 1 para igualar indices
        poste_origen = self._postes[origen - 1]
        poste_destino = self._postes[destino - 1]
                
        # Comprobamos que tengmaos discos en el poste de origen
        assert len(poste_origen) > 0 # hay discos en el poste origen
        disco = poste_origen[-1] # Si tenemos discos extraemos el ultimo, es decir, el de más arriba

        '''
        Comprobamos si podemos realizar el moviiento, si en el poste de destino esta vacio o si el poste de destino no 
        tiene un disco mayor que el que queremos introducir en el
        '''
        assert (len(poste_destino) == 0 # el destino está vacío
                or disco < poste_destino[-1]) # contiene un disco mayor

        # Si todos los assert han sido correctos movemos el disco
        self._discos[disco - 1] = destino
        poste_origen.pop()
        poste_destino.append(disco)
    
    def realiza_movimientos(self, movimientos, imprime=False):
        """
        Realiza varios movimientos, cada movimiento se indica como un par
        (origen, destino).
        """
        
        if imprime:
            self.imprime()
        
        for origen, destino in movimientos:
            self.mueve(origen, destino)
            if imprime:
                print("\n", origen, "->", destino, sep="")
                self.imprime()


    def imprime(self):        
        """Imprime una representación gráfica de las torres"""

        n = len(self)
        for nivel in range(len(self) - 1, -1, -1):
            for poste in self._postes:
                if nivel >= len(poste):
                    print("|", " " * (n - 1), sep="", end=" ")
                else:
                    disco = poste[nivel]
                    print("X" * disco, " " * (n - disco), sep="", end=" ")
            print()
        for _ in self._postes:
            print("=" * n, sep=" ", end=" ")
        print()
        
    def resuelve(self, destino=None):
        """
        Resuelve el problema, moviendo todos los discos al poste destino,
        partiendo de cualquier configuración inicial.
        Si el argumento destino es None, el poste destino es el último.
        Devuelve una secuencia con los movimientos, cada movimiento es un par
        (origen, destino).
        Si hay más de 3 postes, el resto también se deberían utilizar en algunos 
        casos.
        """
        
        '''
        Almacenamos el destino si este no es None, si no se almacena el numero de postes, 
        que hace referencia al utlimo poste ya que en este caso comenzamos a contar desde 1
        '''
        
        destino = destino if destino is not None else self._num_postes
        
        # Creamos una lista en que se llama movimientos y esta vacia
        self._movimientos = []
        
        # Llama a _resuelve y le pasa el resultado de __len__() y el destino
        self._resuelve(len(self), destino)


        return self._movimientos
    

    def _resuelve(self, n, destino):
        # Si no hay discos que mover, salimos
        if n > 0:
            # Origen es el poste donde actualmente está el disco n
            origen = self._discos[n - 1]

            # Si el disco ya está en su sitio final, no hace falta moverlo
            if origen != destino:
                auxiliar = None  # Vamos a buscar un poste auxiliar

                # Recorremos todos los postes para elegir el mejor auxiliar
                for poste in range(1, self._num_postes + 1):
                    # Saltamos si el poste es el de origen o el de destino
                    if poste == origen or poste == destino:
                        continue

                    # Elegimos como auxiliar el primero vacío
                    if not self._postes[poste - 1]:
                        auxiliar = poste
                        break

                    # O el que tenga un disco más grande en la cima
                    if auxiliar is None or self._postes[poste - 1][-1] > self._postes[auxiliar - 1][-1]:
                        auxiliar = poste

                # Paso 1: movemos los n-1 discos más pequeños a un poste auxiliar
                self._resuelve(n - 1, auxiliar)

                # Paso 2: movemos el disco n desde su origen a su destino
                self.mueve(origen, destino)
                self._movimientos.append((origen, destino))

            # Paso 3: finalmente, movemos los n-1 discos desde auxiliar al destino
            self._resuelve(n - 1, destino)



    