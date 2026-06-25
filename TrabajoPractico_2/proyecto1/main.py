# -*- coding: utf-8 -*-
"""
Sala de emergencias

Esta es una adaptación del simulador original provisto por la cátedra
(TP2_problema1/main.py). Se conserva exactamente la misma lógica de
simulación por ciclos (un paciente nuevo por ciclo, atención con 50% de
probabilidad), cambiando únicamente la estructura de almacenamiento de la
cola de espera: en lugar de una lista que atiende siempre al primero en
llegar (FIFO, vía cola_de_espera.pop(0)), se utiliza la ColaPrioridad
(Min-Heap) genérica de la biblioteca, de modo que en cada atención se
seleccione siempre al paciente de mayor urgencia (menor nivel de riesgo)
y, en caso de empate, al que llegó primero.
"""
import sys
import os
import time
import datetime
import random

# Ajuste de ruta para poder importar desde la biblioteca y desde modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'modules')))

import modules.paciente as pac
from biblioteca_ayed_fiuner.ayedfiuner.estructuras.heap import ColaPrioridad

n = 20  # cantidad de ciclos de simulación

"""
Antes: cola_de_espera = list()  --> estructura FIFO original.
Ahora: se reemplaza por la ColaPrioridad genérica (Min-Heap), que
selecciona siempre al paciente más urgente en O(log n).
"""
cola_de_espera = ColaPrioridad()

# Ciclo que gestiona la simulación
for i in range(n):
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')

    print('-*-' * 15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente por ciclo
    # La criticidad del paciente es aleatoria
    paciente = pac.Paciente()
    cola_de_espera.insertar(paciente)

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5 and not cola_de_espera.esta_vacia():
        # Antes: se atendía al paciente que se encontraba al frente de la
        # lista (cola_de_espera.pop(0)), es decir, por orden de llegada.
        # Ahora: se atiende siempre al paciente de mayor prioridad
        # (menor nivel de riesgo); en caso de empate, al que llegó primero.
        paciente_atendido = cola_de_espera.extraer_minimo()
        print('*' * 40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*' * 40)
    else:
        # se continúa atendiendo paciente de ciclo anterior
        pass

    print()
    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', len(cola_de_espera))
    for paciente_pendiente in cola_de_espera:
        print('\t', paciente_pendiente)

    print()
    print('-*-' * 15)
    time.sleep(1)