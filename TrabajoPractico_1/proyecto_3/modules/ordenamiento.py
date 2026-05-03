import sys

class Ordenador:
    """Clase que agrupa los algoritmos de ordenamiento requeridos."""

    @staticmethod
    def burbuja(lista):
        """
        Ordena la lista utilizando el algoritmo de burbuja.
        Pre: 'lista' debe ser una lista de elementos comparables.
        Post: La lista queda ordenada de menor a mayor (In-place).
        """
        if not isinstance(lista, list):
            raise TypeError("Se esperaba una lista para ordenar.")
        
        n = len(lista)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

    @staticmethod
    def quicksort(lista):
        """
        Interfaz para el algoritmo Quicksort.
        Pre: 'lista' debe ser una lista de elementos comparables.
        Post: Devuelve una nueva lista ordenada.
        """
        if not isinstance(lista, list):
            raise TypeError("Se esperaba una lista.")
        return Ordenador._quicksort_recursivo(lista)

    @staticmethod
    def _quicksort_recursivo(lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[len(lista) // 2]
        izq = [x for x in lista if x < pivote]
        centro = [x for x in lista if x == pivote]
        der = [x for x in lista if x > pivote]
        return Ordenador._quicksort_recursivo(izq) + centro + Ordenador._quicksort_recursivo(der)

    @staticmethod
    def radix_sort(lista):
        """
        Ordena la lista utilizando Radix Sort (LSD).
        Pre: 'lista' debe contener números enteros no negativos.
        Post: La lista queda ordenada (In-place).
        """
        if not lista:
            return lista
        
        max_num = max(lista)
        exp = 1
        while max_num // exp > 0:
            Ordenador._counting_sort_for_radix(lista, exp)
            exp *= 10

    @staticmethod
    def _counting_sort_for_radix(lista, exp):
        n = len(lista)
        salida = [0] * n
        conteo = [0] * 10

        for i in range(n):
            indice = (lista[i] // exp) % 10
            conteo[indice] += 1

        for i in range(1, 10):
            conteo[i] += conteo[i - 1]

        i = n - 1
        while i >= 0:
            indice = (lista[i] // exp) % 10
            salida[conteo[indice] - 1] = lista[i]
            conteo[indice] -= 1
            i -= 1

        for i in range(n):
            lista[i] = salida[i]