# -*- coding: utf-8 -*-

class ColaPrioridad:
    """
    Estructura de datos de Cola de Prioridad implementada con un Montículo Binario (Min-Heap).
    Permite insertar elementos y extraer siempre el 'menor' (el de mayor prioridad).
    Complejidad:
        - Inserción: O(log n)
        - Eliminación: O(log n)
    """

    def __init__(self):
        # Usamos una lista para representar el árbol binario completo
        self.__elementos = []

    def esta_vacia(self):
        """Retorna True si la cola no tiene elementos."""
        return len(self.__elementos) == 0

    def __len__(self):
        """Retorna la cantidad de elementos en la cola."""
        return len(self.__elementos)

    def insertar(self, item):
        """
        Agrega un nuevo elemento a la cola.
        Pre: item debe ser comparable con los elementos ya existentes.
        Post: El elemento se ubica en su posición correspondiente según su prioridad.
        """
        self.__elementos.append(item)
        self.__flotar(len(self.__elementos) - 1)

    def extraer_minimo(self):
        """
        Elimina y retorna el elemento con mayor prioridad (el menor).
        Pre: La cola no debe estar vacía.
        Post: Retorna el elemento y reestructura el montículo.
        """
        if self.esta_vacia():
            raise IndexError("Error: Intento de extraer de una cola de prioridad vacía.")
        
        # El mínimo siempre está en la raíz (índice 0)
        # Intercambiamos la raíz con el último elemento para poder eliminarlo
        self.__intercambiar(0, len(self.__elementos) - 1)
        minimo = self.__elementos.pop()
        
        # Si quedó algo, hundimos la nueva raíz para restaurar el orden
        if not self.esta_vacia():
            self.__hundir(0)
            
        return minimo

    def __flotar(self, i):
        """Mueve el elemento en el índice i hacia arriba hasta su lugar."""
        padre = (i - 1) // 2
        # Si el elemento es 'menor' (más prioritario) que su padre, sube
        if i > 0 and self.__elementos[i] < self.__elementos[padre]:
            self.__intercambiar(i, padre)
            self.__flotar(padre)

    def __hundir(self, i):
        """Mueve el elemento en el índice i hacia abajo hasta su lugar."""
        izq = 2 * i + 1
        der = 2 * i + 2
        menor = i
        n = len(self.__elementos)

        # Buscamos cuál es el más pequeño entre el nodo actual y sus hijos
        if izq < n and self.__elementos[izq] < self.__elementos[menor]:
            menor = izq
        if der < n and self.__elementos[der] < self.__elementos[menor]:
            menor = der

        # Si un hijo es menor, intercambiamos y seguimos hundiendo
        if menor != i:
            self.__intercambiar(i, menor)
            self.__hundir(menor)

    def __intercambiar(self, i, j):
        """Método auxiliar para intercambiar dos elementos en la lista."""
        self.__elementos[i], self.__elementos[j] = self.__elementos[j], self.__elementos[i]

    def __str__(self):
        """Representación simple para depuración."""
        return str([str(x) for x in self.__elementos])