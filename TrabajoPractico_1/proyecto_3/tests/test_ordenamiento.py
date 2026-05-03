import unittest
import random
import sys
import os

# Bloque para que el profesor corra el test sin comandos extra desde la raíz
# Agregamos 'proyecto_3' al path para que el import de 'modules' funcione
dir_actual = os.path.dirname(os.path.abspath(__file__))
ruta_proyecto = os.path.abspath(os.path.join(dir_actual, '..'))
if ruta_proyecto not in sys.path:
    sys.path.append(ruta_proyecto)

from modules.ordenamiento import Ordenador

class TestOrdenamiento(unittest.TestCase):
    """Pruebas unitarias para validar los algoritmos de ordenamiento."""

    def setUp(self):
        """Preparamos una lista de 500 números de 5 dígitos (consigna)."""
        self.n = 500
        self.lista_base = [random.randint(10000, 99999) for _ in range(self.n)]
        self.lista_esperada = sorted(self.lista_base)

    def test_burbuja(self):
        """Prueba el algoritmo de burbuja (in-place)."""
        copia = self.lista_base[:]
        Ordenador.burbuja(copia)
        self.assertEqual(copia, self.lista_esperada)

    def test_quicksort(self):
        """Prueba el algoritmo quicksort (devuelve lista nueva)."""
        resultado = Ordenador.quicksort(self.lista_base)
        self.assertEqual(resultado, self.lista_esperada)

    def test_radix_sort(self):
        """Prueba el algoritmo radix sort (in-place)."""
        copia = self.lista_base[:]
        Ordenador.radix_sort(copia)
        self.assertEqual(copia, self.lista_esperada)

    def test_lista_vacia(self):
        """Caso borde: lista vacía."""
        vacia = []
        Ordenador.burbuja(vacia)
        self.assertEqual(vacia, [])
        self.assertEqual(Ordenador.quicksort([]), [])
        Ordenador.radix_sort(vacia)
        self.assertEqual(vacia, [])

if __name__ == '__main__':
    unittest.main()