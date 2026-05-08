# -*- coding: utf-8 -*-
import sys
import os

# Ajuste de ruta para importar la ColaPrioridad del Proyecto 1
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from biblioteca_ayed_fiuner.ayedfiuner.estructuras.heap import ColaPrioridad

def algoritmo_prim(grafo, inicio="Peligros"):
    """
    Calcula el Árbol de Expansión Mínima (MST) utilizando el algoritmo de Prim.
    Pre: El grafo debe estar cargado y el nodo 'inicio' debe existir.
    Post: Retorna una tupla (lista_de_aristas_mst, distancia_total).
    """
    visitados = set()
    mst = []
    distancia_total = 0
    cola = ColaPrioridad() # Reutilización de la estructura genérica

    visitados.add(inicio)
    
    # Insertamos rutas iniciales del origen en la cola (distancia, origen, destino)
    for vecino, peso in grafo.obtener_vecinos(inicio):
        cola.insertar((peso, inicio, vecino))

    while not cola.esta_vacia():
        peso, origen, destino = cola.extraer_minimo()

        if destino not in visitados:
            visitados.add(destino)
            mst.append((origen, destino, peso))
            distancia_total += peso

            # Explorar vecinos del nuevo nodo visitado
            for proximo, proximo_peso in grafo.obtener_vecinos(destino):
                if proximo not in visitados:
                    cola.insertar((proximo_peso, destino, proximo))

    return mst, distancia_total