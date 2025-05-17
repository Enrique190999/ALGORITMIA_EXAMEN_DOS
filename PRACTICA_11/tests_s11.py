import unittest
import sys
import random

if len(sys.argv) > 1:
    file_to_test = sys.argv[1].replace(".py", "")
    code = f'from {file_to_test} import *'
    exec(code)
else:
    from alg_s11 import *


class TestArbolBusquedaOptimo(unittest.TestCase):
    """Tests para la clase ArbolBusquedaOptimo"""
    
    def test_arbol_busqueda_1(self):
        """Tests para la clase ArbolBusquedaOptimo"""
        
        claves = ["k1", "k2", "k3", "k4", "k5"]
        arbol = ArbolBusquedaOptimo(
            claves, [0.15, 0.10, 0.05, 0.10, 0.20], 
            [0.05, 0.10, 0.05, 0.05, 0.05, 0.10])
       
        self.assertEqual(len(arbol), 5)
                              
        for clave in claves:
            self.assertTrue(clave in arbol)
        self.assertTrue("k0" not in arbol)
        self.assertTrue("k6" not in arbol)
        
        for i, clave in enumerate(claves):
            self.assertEqual(arbol[i], clave)
        
        for i, clave in enumerate(arbol):
            self.assertEqual(claves[i], clave)
            
        self.assertEqual(arbol.raiz(), "k2")
        
        self.assertEqual(arbol.profundidad(), 3)
        profundidades = [1, 0, 3, 2, 1]
        for clave, profundidad in zip(claves, profundidades):
            self.assertEqual(arbol.profundidad(clave), profundidad)
            
        lista_hijos = [(None, None), ("k1", "k5"), (None, None), ("k3", None), 
                 ("k4", None)]
        for clave, hijos in zip(claves, lista_hijos):
            self.assertEqual(arbol.hijos(clave), hijos)
            
        self.assertEqual(round(arbol.coste_esperado(), 2), 2.75)
        costes = [ 0.45, 2.75, 0.25, 0.60, 1.30]
        for clave, coste in zip(claves, costes):
            self.assertEqual(round(arbol.coste_esperado(clave), 2), coste)
            
        self.assertEqual(str(arbol), "((k1)k2(((k3)k4)k5))")
        
    def test_arbol_busqueda_2(self):
        """Tests para la clase ArbolBusquedaOptimo"""
        
        claves = ["k" + str(i) for i in range(1, 11)]
        arbol = ArbolBusquedaOptimo(
            claves, 
            [0.21, 0.2, 0.04, 0.06, 0.08, 0.04, 0.04, 0.11, 0.19, 0.03])
    
        self.assertEqual(len(arbol), 10)
                              
        for clave in claves:
            assert clave in arbol
        assert "k0" not in arbol
        assert "k11" not in arbol
        
        for i, clave in enumerate(claves):
            self.assertEqual(arbol[i], clave)
        
        for i, clave in enumerate(arbol):
            self.assertEqual(claves[i], clave)
            
        self.assertEqual(arbol.raiz(), "k2")
        
        self.assertEqual(arbol.profundidad(), 4)
        profundidades = [1, 0, 4, 3, 2, 3, 4, 1, 2, 3]
        for clave, profundidad in zip(claves, profundidades):
            self.assertEqual(arbol.profundidad(clave), profundidad)
        
        lista_hijos = [(None, None), ('k1', 'k8'), (None, None), ('k3', None), 
                       ('k4', 'k6'), (None, 'k7'), (None, None), ('k5', 'k9'), 
                       (None, 'k10'), (None, None)]
        for clave, hijos in zip(claves, lista_hijos):
            self.assertEqual(arbol.hijos(clave), hijos)
            
        self.assertEqual(round(arbol.coste_esperado(), 2), 2.57)
        costes = [0.21, 2.57, 0.04, 0.14, 0.52, 0.12, 0.04, 1.36, 0.25, 0.03]
        for clave, coste in zip(claves, costes):
            self.assertEqual(round(arbol.coste_esperado(clave), 2), coste)
    
        self.assertEqual(str(arbol), "((k1)k2((((k3)k4)k5(k6(k7)))k8(k9(k10))))")        
            

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)