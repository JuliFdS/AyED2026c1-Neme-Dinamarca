# Simulador de Cartas: El Juego de "Guerra"

Breve descripción del proyecto:

Simulación del juego de cartas azaroso "Guerra". El sistema utiliza una Lista Doble Enlazada para gestionar el mazo de cada jugador funcionando bajo una lógica de cola (FIFO) para el reparto y recolección de cartas durante las batallas.

---
## 🏗Arquitectura General

carta.py: Define la clase Carta con lógica de comparación de valores.

mazo.py: Implementa el mazo de los jugadores utilizando la ListaDobleEnlazada personalizada. Define la excepción DequeEmptyError.

juego_guerra.py: Contiene el motor del juego, gestionaando turnos, empates y el estado de "Guerra".

test_juego_guerra.py / test_mazo.py: Conjunto de pruebas unitarias para asegurar la correctitud del flujo.

Las gráficas de los resultados están disponible en la carpeta [data](./data) del proyecto.

El informe completo está disponible en la carpeta [docs](./docs) del proyecto.

---
## 📑Dependencias

1. **Python 3.14**
2. **matplotlib** (`pip install matplotlib`)
3. random (módulo estándar de Python)
4. time (módulo estándar de Python)
5. os / sys (para gestión de rutas)
4. Dependencias listadas en requierements.txt

---
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio.

2. **Crear y activar** un entorno virtual.

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   El archivo `requirements.txt` se encuentran en la carpeta [deps](./deps) del proyecto.

---
## 🙎‍♀️🙎‍♂️Autores

- Dinamarca, Daiana Nicole
- Neme Ferrari del Sel, Julian Bautista

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
