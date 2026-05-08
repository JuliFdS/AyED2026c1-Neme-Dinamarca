import os
# Importamos la clase desde la carpeta modules
from modules.temperaturas_db import Temperaturas_DB

def cargar_muestras_desde_archivo(db):
    """
    Lee las mediciones desde la carpeta data y las carga en la DB.
    """
    # Ruta relativa: desde el raíz hacia la carpeta data
    ruta = os.path.join("data", "muestras.txt")
    
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea and ";" in linea:
                    fecha_str, temp_str = linea.split(';')
                    db.guardar_temperatura(float(temp_str), fecha_str)
        print(f"Éxito: Se cargaron los datos desde {ruta}")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {ruta}. Verifique la carpeta 'data'.")

def app():
    # Instanciamos la base de datos
    db = Temperaturas_DB()
    
    # Cargamos los datos
    cargar_muestras_desde_archivo(db)
    
    # Ejemplo de uso de la interfaz solicitada
    print(f"Cantidad de muestras: {db.cantidad_muestras()}")
    # ... resto de las pruebas solicitadas

if __name__ == "__main__":
    app()