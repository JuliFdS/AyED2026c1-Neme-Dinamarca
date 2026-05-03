# Comparativa de Algoritmos de Ordenamiento

Breve descripción del proyecto:

Implementación y comparación de performance de tres algoritmos de ordenamiento: Burbuja, Quicksort y Radix Sort. Se incluye una comparativa contra el método sorted() nativo de Python.

---
## 🏗Arquitectura General

ordenamiento.py: Clase Ordenador con los métodos estáticos para cada algoritmo.

main.py: Script principal que genera datos aleatorios de 5 dígitos y ejecuta el benchmarking, generando una gráfica comparativa de tiempos bs. tamaño de entrada (N).

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

- Dinamarca Daiana Nicole
- Neme Ferrari del Sel Julian Bautista

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
