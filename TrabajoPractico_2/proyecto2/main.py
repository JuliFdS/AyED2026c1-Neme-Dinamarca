import os
from modules.temperaturas_db import Temperaturas_DB

def cargar_muestras_desde_archivo(db):
    """
    Lee las mediciones desde la carpeta data y las carga en la DB.
    """
    ruta = os.path.join("data", "muestras.txt")
    
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea and ";" in linea:
                    fecha_str, temp_str = linea.split(';')
                    db.guardar_temperatura(temp_str, fecha_str)
        print(f"Éxito: Se cargaron los datos desde {ruta}\n")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {ruta}. Verifique la carpeta 'data'.\n")

def app():
    # Instanciamos la base de datos
    db = Temperaturas_DB()
    
    # Cargamos los datos del archivo
    cargar_muestras_desde_archivo(db)
    
    # --- PRUEBAS DEL TRABAJO PRÁCTICO ---
    print("="*50)
    print("     TESTEO DE INTERFAZ - TEMPERATURAS DB     ")
    print("="*50)

    # 1. Cantidad de muestras
    print(f"1. Cantidad de muestras iniciales: {db.cantidad_muestras()}")
    
    # 2. Devolver una temperatura específica
    fecha_prueba = "26/01/2025" 
    print(f"2. Buscando temperatura para {fecha_prueba}: {db.devolver_temperatura(fecha_prueba)} ºC")
    
    # 3. Guardar una nueva / Actualizar una existente
    print("\n3. Guardando/Actualizando temperaturas...")
    db.guardar_temperatura(24.5, "20/05/2026") # Nueva
    print(f"   Nueva cantidad de muestras: {db.cantidad_muestras()}")
    print(f"   Temperatura actualizada de {fecha_prueba}: {db.devolver_temperatura(fecha_prueba)} ºC")

    # 4. Consultas por Rangos
    f1, f2 = "13/01/2025", "05/03/2025"
    print(f"\n4. Consultas en rango [{f1} inclusive hasta {f2} inclusive]:")
    print(f"   - Temp Máxima en rango: {db.max_temp_rango(f1, f2)} ºC")
    print(f"   - Temp Mínima en rango: {db.min_temp_rango(f1, f2)} ºC")
    
    min_ext, max_ext = db.temp_extremos_rango(f1, f2)
    print(f"   - Extremos (Mín, Máx) en rango: ({min_ext}, {max_ext})")

    # 5. Listado de temperaturas en formato string ordenado
    print(f"\n5. Listado de muestras en rango [{f1} - {f2}]:")
    lista_temps = db.devolver_temperaturas(f1, f2)
    for t in lista_temps:
        print(f"   {t}")

    # 6. Borrado de una temperatura
    print("\n6. Borrando temperatura del 20/05/2026...")
    db.borrar_temperatura("20/05/2026")
    print(f"   Cantidad de muestras final: {db.cantidad_muestras()}")
    print(f"   Buscando la fecha borrada: {db.devolver_temperatura('20/05/2026')}")
    print("="*50)

if __name__ == "__main__":
    app()