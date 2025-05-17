# # Algoritmia
# ## Práctica 6
# En esta práctica se resolverá el problema de las Torres de Hanoi, con dos añadidos: el número de postes puede ser mayor que 3, los discos pueden estar en cualquiera de los postes.

# En el cuerpo de cada función o método a implementar hay una instrucción "pass", se debe sustituir por la implementación adecuada.

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.

class Hanoi:
    """Clase para representar las torres de Hanoi."""

    def __init__(self, discos, num_postes=None):
        if isinstance(discos,int):
            discos = [1] * discos
        else:
            discos = list(discos)
        self._discos = discos
        
        if num_postes is None:
            num_postes = max(3,max(discos))
        self._num_postes = num_postes
        
        self._postes = [[] for _ in range(num_postes)]
        
        longitud_discos = len(discos)
        
        for disco in discos[::-1]:
            self._postes[disco-1].append(longitud_discos)
            longitud_discos -= 1
    
    def mueve(self, origen, destino):
        
        assert 1 <= origen <= self._num_postes
        assert 1 <= destino <= self._num_postes
        
        poste_origen = self._postes[origen - 1]
        poste_destino = self.postes[destino - 1]
        
        assert len(poste_origen) > 0
        disco = poste_origen[-1]
        
        assert (len(poste_destino) == 0 or poste_destino[-1] > disco)
        self._discos[disco-1] = destino
        poste_origen.pop()
        poste_destino.append(disco)

    def resuelve(self, destino=None):
        pass
    
    def _resuelve(self, n, destino):
        pass