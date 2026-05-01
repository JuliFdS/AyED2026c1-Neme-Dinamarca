import time
import matplotlib.pyplot as plt
import sys
import os

# EL PUENTE DE DOS NIVELES
# 1. Ruta de 'proyecto_1'
dir_script = os.path.dirname(os.path.abspath(__file__))

# 2. Subimos a 'TrabajoPractico_1'
dir_tp1 = os.path.dirname(dir_script)

# 3. Subimos a 'AyED2026c1-Neme-Dinamarca'
dir_raiz_catedra = os.path.dirname(dir_tp1)

# 4. Apuntamos a la biblioteca
ruta_biblioteca = os.path.join(dir_raiz_catedra, 'biblioteca_ayed_fiuner')

# Agregamos al sistema
if ruta_biblioteca not in sys.path:
    sys.path.append(ruta_biblioteca)

from ayedfiuner.estructuras.LDE import ListaDobleEnlazada

def realizar_grafica():
    # Definimos tamaños de N (de pequeño a grande)
    # n=10000 es un buen límite para notar la diferencia sin colgar la PC
    tamanios = [100, 500, 1000, 2000, 4000, 6000, 8000, 10000]
    
    tiempos_len = []
    tiempos_copiar = []
    tiempos_invertir = []

    print("Iniciando mediciones...")

    for n in tamanios:
        # Preparamos la lista para la prueba
        lista = ListaDobleEnlazada()
        for i in range(n):
            lista.agregar_al_final(i)
        
        # 1. Medir len() -> O(1)
        # Es tan rápido que lo medimos 1000 veces para tener un promedio real
        t0 = time.perf_counter()
        for _ in range(1000):
            _ = len(lista)
        t1 = time.perf_counter()
        tiempos_len.append((t1 - t0) / 1000)

        # 2. Medir copiar() -> O(n)
        t0 = time.perf_counter()
        lista.copiar()
        t1 = time.perf_counter()
        tiempos_copiar.append(t1 - t0)

        # 3. Medir invertir() -> O(n)
        t0 = time.perf_counter()
        lista.invertir()
        t1 = time.perf_counter()
        tiempos_invertir.append(t1 - t0)
        
        print(f"Procesado N={n}")

    # GENERACIÓN DE LA GRÁFICA-
    plt.figure(figsize=(10, 6))
    
    plt.plot(tamanios, tiempos_len, label='Método len()', color='blue', marker='o')
    plt.plot(tamanios, tiempos_copiar, label='Método copiar()', color='green', marker='s')
    plt.plot(tamanios, tiempos_invertir, label='Método invertir()', color='red', marker='^')

    plt.title('Comparativa de Tiempos de Ejecución: Lista Doble Enlazada')
    plt.xlabel('Cantidad de elementos (N)')
    plt.ylabel('Tiempo (segundos)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Guardar la imagen para el informe antes de mostrarla
    plt.savefig('grafica_rendimiento_LDE.png')
    print("\nGráfica guardada como 'grafica_rendimiento_LDE.png'")
    
    plt.show()

if __name__ == "__main__":
    realizar_grafica()