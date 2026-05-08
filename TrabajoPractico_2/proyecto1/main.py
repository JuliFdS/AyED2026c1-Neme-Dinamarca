# -*- coding: utf-8 -*-
import sys
import os
import time

# Ajuste de ruta para poder importar desde la biblioteca y desde modules
# Esto asegura que Python encuentre tus archivos sin importar desde dónde ejecutes
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'modules')))

from TrabajoPractico_2.proyecto1.modules.paciente import Paciente
from biblioteca_ayed_fiuner.ayedfiuner.estructuras.heap import ColaPrioridad

def simular_sala_emergencias(cantidad_pacientes=10):
    print("="*60)
    print(" SIMULACIÓN DE SALA DE EMERGENCIAS (TRIAJE) ")
    print("="*60)
    
    cola_triage = ColaPrioridad()
    pacientes_ingresados = []

    # 1. Fase de Ingreso (Simulamos la llegada aleatoria)
    print(f"\n[1] Ingresando {cantidad_pacientes} pacientes a la sala...")
    print("-" * 60)
    for _ in range(cantidad_pacientes):
        p = Paciente()  # Se genera con datos aleatorios
        pacientes_ingresados.append(p)
        cola_triage.insertar(p)
        print(f" LLEGADA: {p}")
        # Pequeña pausa para que el contador de tiempo/llegada sea realista
        time.sleep(0.01)

    # 2. Fase de Atención (Aquí se ve la magia de la estructura)
    print("\n" + "="*60)
    print(" ATENCIÓN MÉDICA (ORDEN SEGÚN PRIORIDAD) ")
    print("="*60)
    print("Regla: 1-Crítico > 2-Moderado > 3-Bajo. (Empate -> FIFO)")
    print("-" * 60)

    contador = 1
    while not cola_triage.esta_vacia():
        try:
            paciente_atendido = cola_triage.extraer_minimo()
            print(f" Atendiendo #{contador}: {paciente_atendido}")
            contador += 1
        except IndexError as e:
            print(f"Error inesperado: {e}")

    print("\n" + "="*60)
    print(" Simulación finalizada. Todos los pacientes atendidos. ")
    print("="*60)

if __name__ == "__main__":
    # Puedes cambiar el número para probar con más o menos pacientes
    simular_sala_emergencias(cantidad_pacientes=12)