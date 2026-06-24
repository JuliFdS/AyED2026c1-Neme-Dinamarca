# 🐍 KevinKelvin-DB: Sistema Integrado de Gestión de Muestras Térmicas mediante Árbol AVL

Breve descripción del proyecto:
Este es un sistema de base de datos en memoria principal diseñado específicamente para gestionar de forma eficiente registros masivos de temperaturas asociados a fechas cronológicas. Permite realizar inserciones dinámicas, actualizaciones automáticas, eliminaciones físicas de registros y consultas avanzadas por rangos de fechas (mínimos, máximos y extremos) garantizando tiempos de respuesta optimizados gracias al uso de una estructura de datos auto-balanceada.

---
## 🏗Arquitectura General

El proyecto se encuentra estrictamente organizado bajo un diseño arquitectónico por capas independientes para garantizar la separación de responsabilidades:

1. Capa de Negocio e Interfaz (`modules/temperaturas_db.py`): Define la clase `Temperaturas_DB`, la cual actúa como la interfaz pública del sistema hacia el usuario. Se encarga de procesar las cadenas de texto (`strings`), realizar validaciones mediante bloques `try-except`, parsear fechas y delegar el almacenamiento.
2. Capa de Estructuras de Datos Genéricas (`modules/avl_tree.py`): Contiene las clases `NodoAVL` y `ArbolAVL`. Implementa la lógica matemática pura de un árbol binario balanceado por altura. Es completamente independiente de la lógica del negocio; opera con claves comparables y valores abstractos utilizando rotaciones simples y dobles para mantener su balanceo.
3. Capa de Dominio/Entidades (`modules/mediciones.py`): Define la clase `Medicion`, encargada de empaquetar los atributos de cada muestra científica (objeto `datetime` y valor flotante de temperatura) y formatear su salida textual mediante `__str__`.
4. Capa de Control e Ingreso (`main.py`): Script principal que interactúa con el sistema operativo para realizar la carga masiva desde un archivo de texto (`data/muestras.txt`) y ejecutar las pruebas de regresión de la interfaz.

Las gráficas de los resultados están disponible en la carpeta [data](./data) del proyecto.

El informe completo está disponible en la carpeta [docs](./docs) del proyecto.

---
## 📑Dependencias

1. **Python 3.10+** (Se incluye soporte nativo para tipado estricto y optimizaciones de cadenas).
2. **matplotlib** (`pip install matplotlib`)
3. **datetime** (Módulo integrado de Python para el parseo y manejo cronológico).
4. **os** (Módulo integrado para la gestión de rutas de archivos independientes del sistema operativo).
5. Dependencias de terceros listadas en `requirements.txt` (si existieran librerías como matplotlib para reportes).

---
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio en su máquina local.

2. **Crear y activar** un entorno virtual:
   ```bash
   # En Windows:
   python -m venv venv
   .\venv\Scripts\activate
   
   # En Linux/macOS:
   python3 -m venv venv
   source venv/bin/activate

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   El archivo `requirements.txt` se encuentran en la carpeta [deps](./deps) del proyecto.

---
## 🙎‍♀️🙎‍♂️Autores

- DINAMARCA Daiana Nicole
- NEME Ferrari del Sel Julian Bautista

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
