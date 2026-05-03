# Estructura de Datos: Lista Doble Enlazada (LDE) y Benchmarking

Breve descripción del proyecto:

Implementación desde cero de un TAD (Tipo Abstracto de Datos) de Lista Doble Enlazada en Python. Incluye un análisis empírico de complejidad temporal mediante mediciones de tiempo real para validar la eficiencia teórica de los métodos implementados.

---
## 🏗Arquitectura General

LDE.py: Contiene la clase Nodo y la clase ListaDobleEnlazada. Implementa punteros a la cabeza y a la cola para garantizar operaciones O(1).

benmarking_LDE.py: Script de pruebas de rendimiento que genera gráficas comparativas entre métodos de costo constante (O(1)) y lineal (O(n)).

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
