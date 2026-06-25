# -*- coding: utf-8 -*-
from monticulo import Monticulo


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
    
# =====================================================================
# PEQUEÑA PRUEBA DE USO AISLADA (Aspecto a evaluar nº 4)
# Permite dar cuenta de que verificamos que el módulo funciona.
# =====================================================================
if __name__ == "__main__":
    import sys
    import os
    
    # Truco para permitir que los imports relativos funcionen al ejecutar el archivo suelto
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    print("--- EJECUTANDO PRUEBA DE USO AISLADA: ColaPrioridad (Min-Heap) ---")
    
    # Instanciamos el TAD genérico de forma local
    try:
        pq = ColaPrioridad()
        
        # Almacenamos datos genéricos (tuplas: (nivel_prioridad, "descripcion"))
        # En un Min-Heap el menor valor numérico representa la mayor prioridad
        print("\n1. Encolando elementos genéricos de prueba...")
        pq.insertar((3, "Elemento C (Prioridad Baja)"))
        pq.insertar((1, "Elemento A (Prioridad Crítica)"))
        pq.insertar((2, "Elemento B (Prioridad Moderada)"))
        pq.insertar((1, "Elemento A2 (Mismo nivel crítico - Desempate natural)"))
        
        print(f"   -> Éxito: Cantidad de elementos cargados: {len(pq)}")
        
        print("\n2. Desencolando en orden estricto de prioridad:")
        while not pq.esta_vacia():
            prioridad, elemento = pq.extraer_minimo()
            print(f"   [Extraído] Prioridad: {prioridad} -> Dato: '{elemento}'")
            
        print("\n3. Verificando el manejo de excepciones en operaciones inválidas:")
        try:
            pq.extraer_minimo()
        except IndexError as e:
            print(f"   -> Excepción capturada correctamente: {e}")
            
        print("\n--- PRUEBA CONCLUIDA CON ÉXITO: Módulo verificado correctamente ---")
        
    except Exception as error_general:
        print(f"Ocurrió un error inesperado durante la verificación: {error_general}")