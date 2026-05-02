import time
import matplotlib.pyplot as plt
import sys
import os

# CONFIGURACIÓN DE RUTAS
# 1. Ruta de 'proyecto_1'
dir_script = os.path.dirname(os.path.abspath(__file__))
# 2. Subimos a 'TrabajoPractico_1'
dir_tp1 = os.path.dirname(dir_script)
# 3. Subimos a la raíz del repositorio
dir_raiz_catedra = os.path.dirname(dir_tp1)
# 4. Apuntamos a la biblioteca
ruta_biblioteca = os.path.join(dir_raiz_catedra, 'biblioteca_ayed_fiuner')

# Agregamos la biblioteca al sistema para poder importar LDE
if ruta_biblioteca not in sys.path:
    sys.path.append(ruta_biblioteca)

from ayedfiuner.estructuras.LDE import ListaDobleEnlazada

def realizar_grafica():
    # Consigna: Medir tiempos con listas de tamaño creciente entre 1 y 10000
    tamanios = [100, 500, 1000, 2000, 4000, 6000, 8000, 10000]
    
    tiempos_len = []
    tiempos_copiar = []
    tiempos_invertir = []

    print("Iniciando mediciones de rendimiento...")

    for n in tamanios:
        # Preparamos la lista con N elementos
        lista = ListaDobleEnlazada()
        for i in range(n):
            lista.agregar_al_final(i)
        
        # 1. Medir len() -> Complejidad esperada O(1)
        t0 = time.perf_counter()
        for _ in range(1000):
            _ = len(lista)
        t1 = time.perf_counter()
        tiempos_len.append((t1 - t0) / 1000)

        # 2. Medir copiar() -> Complejidad esperada O(n)[cite: 1]
        t0 = time.perf_counter()
        lista.copiar()
        t1 = time.perf_counter()
        tiempos_copiar.append(t1 - t0)

        # 3. Medir invertir() -> Complejidad esperada O(n)[cite: 1]
        t0 = time.perf_counter()
        lista.invertir()
        t1 = time.perf_counter()
        tiempos_invertir.append(t1 - t0)
        
        print(f"Procesado N={n}")

    # CONFIGURACIÓN DE LA GRÁFICA
    plt.figure(figsize=(10, 6))
    
    plt.plot(tamanios, tiempos_len, label='Método len() - O(1)', color='blue', marker='o')
    plt.plot(tamanios, tiempos_copiar, label='Método copiar() - O(n)', color='green', marker='s')
    plt.plot(tamanios, tiempos_invertir, label='Método invertir() - O(n)', color='red', marker='^')

    plt.title('Comparativa de Tiempos de Ejecución: Lista Doble Enlazada')
    plt.xlabel('Cantidad de elementos (N)')
    plt.ylabel('Tiempo (segundos)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # GUARDADO EN LA CARPETA DOCS
    carpeta_docs = os.path.join(ruta_biblioteca, 'docs')
    
    ruta_guardado = os.path.join(carpeta_docs, 'grafica_rendimiento_LDE.png')
    plt.savefig(ruta_guardado)
    print(f"\nGráfica guardada exitosamente en: {ruta_guardado}")
    
    # Mostrar la gráfica
    plt.show()

if __name__ == "__main__":
    realizar_grafica()