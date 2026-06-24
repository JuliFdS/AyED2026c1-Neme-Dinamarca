from datetime import datetime
from modules.mediciones import Medicion
from modules.arbol_avl import ArbolAVL


class Temperaturas_DB:
    def __init__(self):
        self._arbol = ArbolAVL()
        self.tamanio = 0

    def guardar_temperatura(self, temperatura, fecha_str):
        """
        Guarda la medida de temperatura asociada a la fecha en el árbol AVL.

        Precondición:
            - temperatura: Valor numérico (int o float) o string convertible a float.
            - fecha_str: String que representa una fecha válida en formato "dd/mm/aaaa".
        
        Postcondición:
            - Si los datos son válidos y la fecha no existía, se inserta una nueva Medicion
              y self.tamanio aumenta en 1.
            - Si la fecha ya existía, se actualiza su temperatura y self.tamanio no cambia.
            - El árbol mantiene su propiedad de balanceo AVL.
            - Si los datos son inválidos, el estado de la estructura no cambia.

        Returns:
            None

        Manejo de Excepciones:
            - ValueError: Si fecha_str no cumple el formato o temperatura no es numérica.
                          Se captura internamente y se emite un mensaje de error por consola.
        """
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            nueva_medicion = Medicion(fecha, float(temperatura)) 

            fue_nuevo = self._arbol.insertar(fecha, nueva_medicion)

            if fue_nuevo:
                self.tamanio += 1
        except ValueError:
            print(f"Error de validación: Fecha '{fecha_str}' o temperatura no tienen el formato correcto.")

    def devolver_temperatura(self, fecha_str):
        """
        Obtiene la temperatura registrada para una fecha específica.

        Precondición:
            - fecha_str: String con formato "dd/mm/aaaa".
        
        Postcondición:
            - El estado de Temperaturas_DB permanece inalterado (operación de solo lectura).

        Returns:
            - float: El valor de la temperatura si la fecha se encuentra en el árbol.
            - None: Si la fecha no existe en el árbol o si el formato de fecha_str es inválido.

        Manejo de Excepciones:
            - ValueError: Si fecha_str no cumple el formato. Se captura internamente y retorna None.
        """
        try:
            fecha_dt = datetime.strptime(fecha_str, "%d/%m/%Y")
            medicion = self._arbol.buscar(fecha_dt)
            return medicion.temperatura if medicion else None
        except ValueError:
            return None
        
    def max_temp_rango(self, f1_str, f2_str):
        """
        Devuelve la temperatura máxima dentro del rango de fechas inclusive.

        Precondición:
            - f1_str, f2_str: Strings con formato "dd/mm/aaaa" que representan fechas válidas.
            - Cronológicamente, f1_str <= f2_str.
        
        Postcondición:
            - El estado del árbol y self.tamanio permanecen inalterados.

        Returns:
            - float: La temperatura máxima encontrada en el intervalo cerrado [f1, f2].
            - None: Si no hay muestras en ese rango o si los formatos de fecha son inválidos.

        Manejo de Excepciones:
            - ValueError: Captura formatos incorrectos en las fechas de rango y retorna None.
        """
        temps = self._obtener_lista_rango(f1_str, f2_str)
        return max(temps) if temps else None

    def min_temp_rango(self, fecha1_str, fecha2_str):
        """
        Devuelve la temperatura mínima dentro del rango de fechas inclusive.

        Precondición:
            - f1_str, f2_str: Strings con formato "dd/mm/aaaa" que representan fechas válidas.
            - Cronológicamente, f1_str <= f2_str.

        Postcondición:
            - El estado del árbol y self.tamanio permanecen inalterados.

        Returns:
            - float: La temperatura mínima encontrada en el intervalo cerrado [f1, f2].
            - None: Si no hay muestras en ese rango o si los formatos de fecha son inválidos.

        Manejo de Excepciones:
            - ValueError: Captura formatos incorrectos en las fechas de rango y retorna None.
        """
        temps = self._obtener_lista_rango(fecha1_str, fecha2_str)
        return min(temps) if temps else None

    def temp_extremos_rango(self, fecha1_str, fecha2_str):
        """
        Devuelve la temperatura mínima y máxima encontradas dentro del rango de fechas inclusive.

        Precondición:
            - fecha1_str, fecha2_str: Strings con formato "dd/mm/aaaa" que representan fechas válidas.
            - Cronológicamente, fecha1_str <= fecha2_str.
        
        Postcondición:
            - El estado interno de Temperaturas_DB y self.tamanio permanecen inalterados.

        Returns:
            - tuple(float, float): Una tupla con la temperatura mínima y la máxima en ese intervalo cerrado.
            - tuple(None, None): Si no existen mediciones en el rango o si los formatos de fecha son inválidos.

        Manejo de Excepciones:
            - ValueError: Capturado indirectamente en _obtener_lista_rango. Evita la falla y retorna (None, None).
        """
        temps = self._obtener_lista_rango(fecha1_str, fecha2_str)
        return (min(temps), max(temps)) if temps else (None, None)

    def borrar_temperatura(self, fecha_str):
        """
        Recibe una fecha y elimina de la estructura la medición correspondiente a esa fecha.

        Precondición:
            - fecha_str: String con formato "dd/mm/aaaa".
        
        Postcondición:
            - Si la fecha existe en el árbol, se elimina su nodo, disminuyendo self.tamanio en 1.
            - La estructura de Temperaturas_DB se reestructura preservando el balanceo del árbol AVL.
            - Si la fecha no existe o el formato es inválido, el estado de la estructura y self.tamanio no cambian.

        Returns:
            None

        Manejo de Excepciones:
            - ValueError: Captura formatos inválidos de fecha_str, aborta la eliminación y muestra un mensaje por consola.
        """
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            se_elimino = self._arbol.eliminar(fecha)
            if se_elimino:
                self.tamanio -= 1
            else:
                print(f"La fecha {fecha_str} no existe en la base de datos.")
        except ValueError:
            print("Error: Formato de fecha inválido para eliminación.")

    def devolver_temperaturas(self, f1_str, f2_str):
        """
        Devuelve un listado de las mediciones de temperatura en el rango recibido por parámetro.

        Precondición:
            - f1_str, f2_str: Strings con formato "dd/mm/aaaa" que representan fechas válidas.
        
        Postcondición:
            - El estado de la estructura de datos permanece inalterado.

        Returns:
            - list[str]: Un listado de cadenas de caracteres, donde cada elemento cumple el formato 
                         “dd/mm/aaaa: temperatura ºC”, ordenado cronológicamente por sus fechas.
            - list[]: Una lista vacía si no hay registros en el rango indicado o si hay errores de formato.

        Manejo de Excepciones:
            - ValueError: Captura formatos de fecha incorrectos y mitiga la excepción retornando una lista vacía.
        """
        try:
            f1 = datetime.strptime(f1_str, "%d/%m/%Y")
            f2 = datetime.strptime(f2_str, "%d/%m/%Y")
            resultados = []
            mediciones_en_rango = self._arbol.obtener_rango(f1, f2)
            return [str(m) for m in mediciones_en_rango]
        except ValueError:
            return []

    def cantidad_muestras(self):
        """
        Devuelve la cantidad total de muestras almacenadas en la base de datos.

        Precondición:
            Ninguna.
        
        Postcondición:
            - El estado de Temperaturas_DB permanece inalterado.

        Returns:
            - int: Valor del atributo self.tamanio que representa la cantidad actual de nodos en el árbol.
        """
        return self.tamanio

    # Método auxilar

    def _obtener_lista_rango(self, f1_str, f2_str):
        try:
            f1 = datetime.strptime(f1_str, "%d/%m/%Y")
            f2 = datetime.strptime(f2_str, "%d/%m/%Y")
            mediciones = self._arbol.obtener_rango(f1, f2)
            return [m.temperatura for m in mediciones]
        except ValueError:
            return []