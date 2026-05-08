# -*- coding: utf-8 -*-
import os
import sys

# Ajuste de rutas para importaciones
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from biblioteca_ayed_fiuner.ayedfiuner.estructuras.grafo import Grafo
from modules.logica_palomas import algoritmo_prim

def cargar_datos_aldeas(nombre_archivo):
    """
    Lee el archivo txt y construye el grafo.
    Pre: El archivo debe existir y tener formato 'Origen, Destino, Distancia'.
    Post: Retorna un objeto Grafo cargado.
    """
    grafo = Grafo()
    # Buscamos el archivo en la carpeta data relativa a este main.py
    ruta = os.path.join(os.path.dirname(__file__), 'data', nombre_archivo)
    
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encontró el archivo de datos en: {ruta}")

    with open(ruta, 'r', encoding='utf-8') as f:
        for num_linea, linea in enumerate(f, 1):
            linea = linea.strip()
            if not linea: continue
            
            partes = linea.split(',')
            if len(partes) == 3:
                try:
                    a1, a2, dist = partes[0].strip(), partes[1].strip(), int(partes[2].strip())
                    grafo.agregar_ruta(a1, a2, dist)
                except ValueError:
                    print(f"Advertencia: Error de formato en línea {num_linea}. Omitiendo.")
            # Si la línea tiene un solo nombre (como Diosleguarde), solo la agregamos como nodo
            elif len(partes) == 1:
                grafo.agregar_aldea(partes[0].strip())
    return grafo

def ejecutar_mision():
    try:
        grafo = cargar_datos_aldeas('aldeas.txt')
        
        # 1. Mostrar aldeas en orden alfabético
        aldeas_ordenadas = sorted(grafo.obtener_aldeas())
        print("="*80)
        print("SISTEMA DE COMUNICACIÓN: PALOMAS WILLIAM")
        print("="*80)
        print(f"Aldeas registradas ({len(aldeas_ordenadas)}):")
        print(", ".join(aldeas_ordenadas))
        print("-" * 80)

        # 2. Ejecutar Prim para eficiencia máxima
        rutas_mst, total_leguas = algoritmo_prim(grafo, "Peligros")

        # Mapear relaciones emisor-receptor
        relaciones = {a: {'padre': None, 'hijos': []} for a in aldeas_ordenadas}
        for origen, destino, peso in rutas_mst:
            relaciones[destino]['padre'] = origen
            relaciones[origen]['hijos'].append(destino)

        # Mostrar tabla de distribución
        print(f"{'ALDEA':<20} | {'RECIBE NOTICIA DE':<20} | {'ENVÍA RÉPLICAS A'}")
        print("-" * 80)
        for aldea in aldeas_ordenadas:
            recibe = relaciones[aldea]['padre']
            if aldea == "Peligros":
                recibe_str = "(Punto de Origen)"
            else:
                recibe_str = recibe if recibe else "DESCONECTADA"
            
            envia_str = ", ".join(relaciones[aldea]['hijos']) if relaciones[aldea]['hijos'] else "---"
            print(f"{aldea:<20} | {recibe_str:<20} | {envia_str}")

        # 3. Mostrar distancia total
        print("-" * 80)
        print(f"SUMA TOTAL DE DISTANCIAS RECORRIDAS: {total_leguas} leguas.")
        print("="*80)

    except Exception as e:
        print(f"Error crítico en la ejecución: {e}")

if __name__ == "__main__":
    ejecutar_mision()