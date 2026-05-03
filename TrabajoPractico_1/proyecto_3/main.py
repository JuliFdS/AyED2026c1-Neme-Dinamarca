import time
import random
import matplotlib.pyplot as plt
import sys
import os

# BLOQUE PARA QUE EL PROFE CORRA DESDE LA RAÍZ
dir_actual = os.path.dirname(os.path.abspath(__file__))
ruta_proyecto = os.path.abspath(os.path.join(dir_actual, '..', '..'))
if ruta_proyecto not in sys.path:
    sys.path.append(ruta_proyecto)

# Importamos desde tu estructura de carpetas
from TrabajoPractico_1.proyecto_3.modules.ordenamiento import Ordenador

def medir_tiempos():
    # Tamaños de 1 a 1000 con saltos de 50
    tamanos = range(1, 1001, 50) 
    tiempos_burbuja = []
    tiempos_quick = []
    tiempos_radix = []
    tiempos_sorted = [] # Agregamos el built-in de Python

    for n in tamanos:
        # Generar lista de n números de 5 dígitos (mínimo 500 según consigna)
        lista_orig = [random.randint(10000, 99999) for _ in range(n)]
        
        # Medir Burbuja
        copia = lista_orig[:]
        start = time.perf_counter()
        Ordenador.burbuja(copia)
        tiempos_burbuja.append(time.perf_counter() - start)
        
        # Medir Quick
        copia = lista_orig[:]
        start = time.perf_counter()
        Ordenador.quicksort(copia)
        tiempos_quick.append(time.perf_counter() - start)

        # Medir Radix
        copia = lista_orig[:]
        start = time.perf_counter()
        Ordenador.radix_sort(copia)
        tiempos_radix.append(time.perf_counter() - start)

        # Medir Sorted (Built-in)
        copia = lista_orig[:]
        start = time.perf_counter()
        sorted(copia)
        tiempos_sorted.append(time.perf_counter() - start)

    # Graficar resultados
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos_burbuja, label='Burbuja (O(n²))', color='blue')
    plt.plot(tamanos, tiempos_quick, label='Quicksort (O(n log n))', color='orange')
    plt.plot(tamanos, tiempos_radix, label='Radix Sort (O(nk))', color='green')
    plt.plot(tamanos, tiempos_sorted, label='Python Sorted (Timsort)', color='red', linestyle='--')
    
    plt.xlabel('Tamaño de la lista (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de Algoritmos de Ordenamiento')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    medir_tiempos()