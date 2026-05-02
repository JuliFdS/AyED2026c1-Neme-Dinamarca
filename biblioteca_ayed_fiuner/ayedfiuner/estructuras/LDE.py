class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    """
    Implementación del TAD Lista Doblemente Enlazada para el Problema 1.
    Permite almacenar elementos comparables y respeta la especificación lógica.
    """
    
    def __init__(self):
        """
        Consigna: El inicializador __init__ debe crear una lista originalmente vacía.
        """
        self._cabeza = None
        self._cola = None
        self._tamanio = 0

    # --- Consigna: El acceso a atributos debe realizarse con decoradores properties ---
    @property
    def cabeza(self):
        """Devuelve el atributo privado cabeza con @property"""
        return self._cabeza

    @cabeza.setter
    def cabeza(self, nuevo_nodo):
        self._cabeza = nuevo_nodo

    @property
    def cola(self):
        """Devuelve el atributo privado cola con @property"""
        return self._cola

    @cola.setter
    def cola(self, nuevo_nodo):
        self._cola = nuevo_nodo

    @property
    def tamanio(self):
        return self._tamanio

    @tamanio.setter
    def tamanio(self, valor):
        self._tamanio = valor

    def esta_vacia(self):
        """esta_vacia(): Devuelve True si la lista está vacía."""
        return self.tamanio == 0

    def agregar_al_inicio(self, item):
        """agregar_al_inicio(item): Agrega un nuevo ítem al inicio de la lista."""
        nuevo_nodo = Nodo(item)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamanio += 1

    def agregar_al_final(self, item):
        """agregar_al_final(item): Agrega un nuevo ítem al final de la lista."""
        nuevo_nodo = Nodo(item)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamanio += 1

    def insertar(self, item, posicion=None):
        """
        insertar(item, posicion): Agrega un nuevo ítem a la lista en 'posicion'.
        Si la posición no se pasa, se añade al final.
        Arroja excepción si la posición es inválida.
        """
        # Consigna: Si la posición no se pasa, añadir al final
        if posicion is None:
            self.agregar_al_final(item)
            return

        # Consigna: Si se quiere insertar en posición inválida, arrojar excepción
        if not isinstance(posicion, int) or posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición fuera de rango o inválida")
        
        if posicion == 0:
            self.agregar_al_inicio(item)
        elif posicion == self.tamanio:
            self.agregar_al_final(item)
        else:
            nuevo_nodo = Nodo(item)
            # Uso de método auxiliar optimizado O(n/2)
            nodo_actual = self._get_nodo(posicion)
            nodo_anterior = nodo_actual.anterior

            nuevo_nodo.siguiente = nodo_actual
            nuevo_nodo.anterior = nodo_anterior

            nodo_anterior.siguiente = nuevo_nodo
            nodo_actual.anterior = nuevo_nodo
            self.tamanio += 1

    def extraer(self, posicion=None):
        """
        extraer(posicion): elimina y devuelve el ítem en 'posicion'.
        Si no se indica, elimina el último.
        Complejidad en extremos debe ser O(1).
        """
        if self.esta_vacia():
            raise IndexError("La lista está vacía")
        
        # Consigna: Si no se indica posición, se elimina el último
        if posicion is None:
            posicion = self.tamanio - 1
        
        # Consigna: Si se quiere extraer de posición indebida, arrojar excepción
        if not isinstance(posicion, int) or posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Posición fuera de rango o inválida")
        
        # Consigna: Complejidad O(1) en extremos
        if posicion == 0: # Inicio O(1)
            nodo_extraido = self.cabeza
            dato = nodo_extraido.dato
            self.cabeza = nodo_extraido.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
            self.tamanio -= 1
            return dato

        if posicion == self.tamanio - 1: # Final O(1)
            nodo_extraido = self.cola
            dato = nodo_extraido.dato
            self.cola = nodo_extraido.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
            self.tamanio -= 1
            return dato

        # Caso general (posiciones intermedias)
        nodo_extraido = self._get_nodo(posicion)
        dato = nodo_extraido.dato
        nodo_extraido.anterior.siguiente = nodo_extraido.siguiente
        nodo_extraido.siguiente.anterior = nodo_extraido.anterior
        
        self.tamanio -= 1
        return dato

    def _get_nodo(self, posicion):
        """Método auxiliar para obtener el nodo, optimizado para recorrer desde el extremo más cercano."""
        if posicion < self.tamanio // 2:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
        else:
            actual = self.cola
            for _ in range(self.tamanio - 1, posicion, -1):
                actual = actual.anterior
        return actual

    def copiar(self):
        """
        copiar(): Realiza una copia elemento a elemento y devuelve la copia.
        Consigna: Verificar que el orden sea O(n) y no O(n^2).
        """
        nueva_lista = ListaDobleEnlazada()
        actual = self.cabeza
        while actual:
            # Como agregar_al_final es O(1), el bucle total es O(n)
            nueva_lista.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return nueva_lista

    def invertir(self):
        """invertir(): Invierte el orden de los elementos de la lista."""
        if self.esta_vacia() or self.tamanio == 1:
            return
        
        actual = self.cabeza
        self.cola = actual 
        temporal = None
        
        while actual:
            temporal = actual.anterior
            actual.anterior = actual.siguiente
            actual.siguiente = temporal
            actual = actual.anterior # Avanza usando el puntero anterior (que ahora es el original siguiente)
        
        if temporal:
            self.cabeza = temporal.anterior

    def concatenar(self, otra_lista):
        """
        concatenar(Lista): Recibe una lista y la concatena al final de la actual.
        """
        for item in otra_lista:
            self.agregar_al_final(item)
        return self
    
    def __len__(self):
        """__len__(): Devuelve el número de ítems de la lista."""
        return self.tamanio

    def __add__(self, otra_lista):
        """
        __add__(Lista): Suma dos listas devolviendo una nueva.
        Aprovecha concatenar para evitar repetir código.
        """
        nueva = self.copiar()
        return nueva.concatenar(otra_lista)
    
    def __iter__(self):
        """__iter__(): Permite que la lista sea recorrida con un ciclo for."""
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente