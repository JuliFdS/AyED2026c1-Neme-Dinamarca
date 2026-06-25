# -*- coding: utf-8 -*-

class Monticulo:
    """
    TAD Montículo Binario (Min-Heap).

    Estructura de datos de bajo nivel que mantiene un conjunto de elementos
    comparables organizados en un árbol binario casi completo, representado
    internamente mediante una lista, de modo que el elemento "menor" (más
    prioritario, según el operador < de los elementos) siempre se encuentra
    en la raíz.

    Esta clase es completamente genérica: no conoce nada sobre el dominio
    de los elementos que almacena, solamente requiere que sean comparables
    entre sí. Expone las operaciones estructurales propias de un montículo
    (insertar, extraer el mínimo, flotar, hundir).

    Complejidad:
        - Inserción: O(log n)
        - Extracción del mínimo: O(log n)
    """

    def __init__(self):
        # Usamos una lista para representar el árbol binario completo
        self._elementos = []

    def esta_vacio(self):
        """Retorna True si el montículo no tiene elementos."""
        return len(self._elementos) == 0

    def __len__(self):
        """Retorna la cantidad de elementos en el montículo."""
        return len(self._elementos)

    def __iter__(self):
        """
        Permite recorrer los elementos actualmente almacenados sin
        extraerlos (de solo lectura). No garantiza ningún orden de
        prioridad en el recorrido.
        """
        return iter(self._elementos)

    def insertar(self, item):
        """
        Agrega un nuevo elemento al montículo.
        Pre: item debe ser comparable con los elementos ya existentes.
        Post: El elemento se ubica en su posición correspondiente,
              preservando la propiedad de montículo mínimo.
        """
        self._elementos.append(item)
        self._flotar(len(self._elementos) - 1)

    def extraer_minimo(self):
        """
        Elimina y retorna el elemento "menor" (la raíz del montículo).
        Pre: El montículo no debe estar vacío.
        Post: Retorna el elemento extraído y reestructura el montículo
              para preservar la propiedad de orden.
        """
        if self.esta_vacio():
            raise IndexError("Error: Intento de extraer de un montículo vacío.")

        # El mínimo siempre está en la raíz (índice 0)
        # Intercambiamos la raíz con el último elemento para poder eliminarlo
        self._intercambiar(0, len(self._elementos) - 1)
        minimo = self._elementos.pop()

        # Si quedó algo, hundimos la nueva raíz para restaurar el orden
        if not self.esta_vacio():
            self._hundir(0)

        return minimo

    def _flotar(self, i):
        """Mueve el elemento en el índice i hacia arriba hasta su lugar."""
        padre = (i - 1) // 2
        # Si el elemento es 'menor' (más prioritario) que su padre, sube
        if i > 0 and self._elementos[i] < self._elementos[padre]:
            self._intercambiar(i, padre)
            self._flotar(padre)

    def _hundir(self, i):
        """Mueve el elemento en el índice i hacia abajo hasta su lugar."""
        izq = 2 * i + 1
        der = 2 * i + 2
        menor = i
        n = len(self._elementos)

        # Buscamos cuál es el más pequeño entre el nodo actual y sus hijos
        if izq < n and self._elementos[izq] < self._elementos[menor]:
            menor = izq
        if der < n and self._elementos[der] < self._elementos[menor]:
            menor = der

        # Si un hijo es menor, intercambiamos y seguimos hundiendo
        if menor != i:
            self._intercambiar(i, menor)
            self._hundir(menor)

    def _intercambiar(self, i, j):
        """Método auxiliar para intercambiar dos elementos en la lista."""
        self._elementos[i], self._elementos[j] = self._elementos[j], self._elementos[i]

    def __str__(self):
        """Representación simple para depuración."""
        return str([str(x) for x in self._elementos])