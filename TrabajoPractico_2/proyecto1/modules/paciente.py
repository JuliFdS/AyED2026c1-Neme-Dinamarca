
from random import randint, choices

# Datos para la generación aleatoria (Originales)
nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# Probabilidades: 10% crítico, 30% moderado, 60% bajo
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    """
    Representa a un paciente en el sistema de triaje.
    La prioridad se define por el nivel de riesgo (1 < 2 < 3).
    Si dos pacientes tienen igual riesgo, se utiliza el orden de llegada (FIFO).
    """
    
    # Atributo de clase: Contador global para el segundo criterio de selección
    __contador_llegada = 0

    def __init__(self, nombre=None, apellido=None, riesgo=None):
        # Si no se pasan datos, se generan aleatoriamente
        n = len(nombres)
        self.__nombre = nombre if nombre else nombres[randint(0, n-1)]
        self.__apellido = apellido if apellido else apellidos[randint(0, n-1)]
        self.__riesgo = riesgo if riesgo else choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        
        # Lógica de llegada: Cada paciente nuevo incrementa el contador global
        Paciente.__contador_llegada += 1
        self.__orden_llegada = Paciente.__contador_llegada

    # --- Getters ---
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_descripcion_riesgo(self):
        return self.__descripcion

    def get_orden_llegada(self):
        return self.__orden_llegada

    # --- Métodos de Comparación para el TAD Genérico ---
    # Estos permiten que el Heap ordene pacientes sin conocer sus atributos internos

    def __lt__(self, otro):
        """
        Sobrecarga del operador '<' (Less Than).
        Indica si este paciente tiene más prioridad que 'otro'.
        """
        # Criterio 1: Riesgo (1 es más prioritario que 2)
        if self.__riesgo != otro.__riesgo:
            return self.__riesgo < otro.__riesgo
        
        # Criterio 2: Si el riesgo es igual, el que llegó antes (menor orden) va primero
        return self.__orden_llegada < otro.__orden_llegada

    def __eq__(self, otro):
        """Sobrecarga del operador '=='."""
        return (self.__riesgo == otro.__riesgo and 
                self.__orden_llegada == otro.__orden_llegada)

    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        cad += f' (orden de llegada: {self.__orden_llegada})'
        return cad