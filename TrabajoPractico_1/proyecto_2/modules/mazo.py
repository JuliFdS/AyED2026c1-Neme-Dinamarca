# -*- coding: utf-8 -*-
import sys
import os

# BLOQUE DE COMPATIBILIDAD (Para que el profesor pueda darle a "Play" sin configurar nada)
dir_actual = os.path.dirname(os.path.abspath(__file__))
# Subimos niveles para llegar a la raíz y encontrar la biblioteca
ruta_biblio = os.path.abspath(os.path.join(dir_actual, '..', '..', '..', 'biblioteca_ayed_fiuner'))
if ruta_biblio not in sys.path:
    sys.path.append(ruta_biblio)

from ayedfiuner.estructuras.LDE import ListaDobleEnlazada
from modules.carta import Carta

class DequeEmptyError(Exception):
    """Excepción lanzada cuando se intenta extraer de un mazo vacío."""
    pass

class Mazo:
    """
    TAD Mazo que utiliza una Lista Doble Enlazada para almacenar objetos Carta.
    Respetamos estrictamente los métodos que llama 'juego_guerra.py'.
    """
    def __init__(self):
        """Post: Inicializa un mazo vacío usando la LDE del Problema 1."""
        self._cartas = ListaDobleEnlazada()

    def poner_carta_arriba(self, carta):
        """Agrega una carta al inicio del mazo."""
        self._cartas.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        """Agrega una carta al final del mazo."""
        self._cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        """
        Extrae la carta de arriba. Lanza DequeEmptyError si está vacío.
        Si 'mostrar' es True, hace la carta visible.
        """
        if self._cartas.esta_vacia():
            raise DequeEmptyError("El mazo está vacío.")
        
        carta = self._cartas.extraer(0)
        if mostrar:
            carta.visible = True
        return carta

    def __len__(self):
        """Post: Devuelve la cantidad de cartas en el mazo."""
        return len(self._cartas)

    def __str__(self):
        """
        Post: Devuelve las cartas separadas por espacio.
        Corregido: Evitamos 'get_node' para prevenir el AttributeError.
        """
        try:
            # Intentamos iterar sobre la LDE (asumiendo que tiene __iter__)
            return " ".join(str(carta) for carta in self._cartas)
        except TypeError:
            # Si tu LDE no es iterable, usamos su representación por defecto
            # para que el 'print' en el juego no falle.
            return str(self._cartas)