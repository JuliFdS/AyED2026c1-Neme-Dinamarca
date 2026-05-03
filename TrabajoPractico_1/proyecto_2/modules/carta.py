# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 16:51:54 2022

@author: Cátedra de Algoritmos y Estructura de Datos
"""
# -*- coding: utf-8 -*-
class Carta:
    def __init__(self, valor='', palo=''):
        self.valor = valor
        self.palo = palo
        self._visible = False  # Cambiado para coincidir con la propiedad

    @property
    def visible(self):
        return self._visible
        
    @visible.setter
    def visible(self, visible):
        self._visible = visible
        
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, valor):
        self._valor = valor
        
    @property
    def palo(self):
        return self._palo
    
    @palo.setter
    def palo(self, palo):
        self._palo = palo  
    
    def _valor_numerico(self):
        """Convierte J, Q, K, A a valores 11-14 para comparaciones."""
        valores_letras = ['J','Q','K','A']
        if self.valor in valores_letras:
            idx = valores_letras.index(self.valor)
            return (11 + idx)
        return int(self.valor)            
            
    def __gt__(self, otra):
        """Compara si una carta es mayor a otra por valor numérico."""
        return self._valor_numerico() > otra._valor_numerico()
    
    def __eq__(self, otra):
        """Necesario para detectar el estado de 'Guerra' (empate)."""
        return self._valor_numerico() == otra._valor_numerico()
        
    def __str__(self):
        if not self.visible:
            return "-X"
        return f"{self.valor}{self.palo}"
    
    def __repr__(self):
        return str(self)

if __name__ == "__main__":
    # Corregido: Valor primero, luego Palo
    carta = Carta("3", "♣")
    carta.visible = True
    print(f"Carta de prueba: {carta}")