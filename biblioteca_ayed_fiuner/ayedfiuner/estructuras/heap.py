# -*- coding: utf-8 -*-
from .monticulo import Monticulo


class ColaPrioridad:
    """
    TAD Cola de Prioridad.

    Estructura de datos que permite insertar elementos y extraer siempre
    el de mayor prioridad (el "menor", según el operador < de los
    elementos almacenados).

    Esta clase NO implementa por sí misma la lógica de un montículo
    binario: en su lugar, utiliza por composición un Monticulo (ver
    ayedfiuner.estructuras.monticulo), delegándole todo el trabajo
    estructural. De este modo, ColaPrioridad encapsula el funcionamiento
    interno del montículo y expone únicamente la interfaz propia de una
    cola de prioridad. Si en el futuro se decidiera cambiar la
    implementación interna (por ejemplo, usar una lista ordenada o un
    árbol balanceado en lugar de un montículo), el código que utiliza
    ColaPrioridad no se vería afectado.

    Complejidad (heredada del Monticulo subyacente):
        - Inserción: O(log n)
        - Eliminación: O(log n)
    """

    def __init__(self):
        # Composición: la Cola de Prioridad utiliza internamente un
        # Montículo, pero no lo expone hacia afuera.
        self.__monticulo = Monticulo()

    def esta_vacia(self):
        """Retorna True si la cola no tiene elementos."""
        return self.__monticulo.esta_vacio()

    def __len__(self):
        """Retorna la cantidad de elementos en la cola."""
        return len(self.__monticulo)

    def __iter__(self):
        """
        Permite recorrer los elementos actualmente en la cola sin extraerlos
        (de solo lectura). No garantiza orden de prioridad en el recorrido,
        solo expone el contenido interno de la cola para fines de
        visualización (por ejemplo, listar los pacientes pendientes).
        """
        return iter(self.__monticulo)

    def insertar(self, item):
        """
        Agrega un nuevo elemento a la cola.
        Pre: item debe ser comparable con los elementos ya existentes.
        Post: El elemento se ubica en su posición correspondiente según su prioridad.
        """
        self.__monticulo.insertar(item)

    def extraer_minimo(self):
        """
        Elimina y retorna el elemento con mayor prioridad (el menor).
        Pre: La cola no debe estar vacía.
        Post: Retorna el elemento y reestructura la cola internamente.
        """
        if self.esta_vacia():
            raise IndexError("Error: Intento de extraer de una cola de prioridad vacía.")
        return self.__monticulo.extraer_minimo()

    def __str__(self):
        """Representación simple para depuración."""
        return str(self.__monticulo)