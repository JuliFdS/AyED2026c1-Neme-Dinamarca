# -*- coding: utf-8 -*-

class Grafo:
    """
    Representación de un grafo pesado no dirigido mediante listas de adyacencia.
    """
    def __init__(self):
        # Diccionario: { aldea: [(vecino, distancia), ...] }
        self.__adyacencias = {}

    def agregar_aldea(self, nombre):
        """
        Agrega un nuevo vértice al grafo si no existe.
        Pre: nombre debe ser un string.
        Post: Se crea una entrada en el diccionario de adyacencias.
        """
        if nombre not in self.__adyacencias:
            self.__adyacencias[nombre] = []

    def agregar_ruta(self, aldea1, aldea2, distancia):
        """
        Agrega una conexión bidireccional con un peso (distancia).
        Pre: distancia debe ser un entero positivo.
        Post: Ambas aldeas quedan conectadas en el grafo.
        """
        self.agregar_aldea(aldea1)
        self.agregar_aldea(aldea2)
        self.__adyacencias[aldea1].append((aldea2, distancia))
        self.__adyacencias[aldea2].append((aldea1, distancia))

    def obtener_aldeas(self):
        """Retorna una lista con los nombres de todas las aldeas."""
        return list(self.__adyacencias.keys())

    def obtener_vecinos(self, aldea):
        """Retorna la lista de tuplas (vecino, distancia) de una aldea."""
        return self.__adyacencias.get(aldea, [])