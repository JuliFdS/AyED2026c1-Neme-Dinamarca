class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
    
    """
    esta_vacia(): Devuelve True si la lista está vacía.
    """
    def esta_vacia(self):
        if self.tamanio == 0:
            return True
    
    
    """
    agregar_al_inicio(item): Agrega un nuevo ítem al inicio de la lista.
    """
    def agregar_al_inicio(self, item):
        nuevo_nodo = Nodo(item)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamanio += 1

    """
    agregar_al_final(item): Agrega un nuevo ítem al final de la lista.
    """
    def agregar_al_final(self, item):
        nuevo_nodo = Nodo(item)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamanio += 1
    
    """
    insertar(item, posicion): Agrega un nuevo ítem a la lista en "posicion".
    Si la posición no se pasa como argumento, el ítem debe añadirse al final de la lista.
    "posicion" es un entero que indica la posición en la lista donde se va a insertar el nuevo elemento.
    Si se quiere insertar en una posición inválida, que se arroje la debida excepción.
    """
    def insertar (item, posicion=None):
        
        #Si no se especifica una posición, se agrega al final de la lista
        if posicion == None:
            self.agregar_al_final(item)

        #Valida que la posición sea un número entero dentro del rango válido
        if posicion < 0 or posicion > self.tamanio or not isinstance(posicion, int):
            raise IndexError("Posición fuera de rango o inválida")
        
        nuevo_nodo = Nodo(item)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        elif posicion == 0:
            self.agregar_al_inicio(nuevo_nodo)
        elif posicion == self.tamanio:
            self.agregar_al_final(nuevo_nodo)
        else:
            nodo_actual = self._get_nodo(posicion)
            nodo_anterior = nodo_actual.anterior

            nuevo_nodo.siguiente = nodo_actual
            nuevo_nodo.anterior = nodo_anterior

            nodo_anterior.siguiente = nuevo_nodo
            nodo_actual.anterior = nuevo_nodo
        self.tamanio += 1

    """
    extraer(posicion): elimina y devuelve el ítem en "posición".
    Si no se indica el parámetro posición, se elimina y devuelve el último elemento de la lista.
    La complejidad de extraer elementos de los extremos de la lista debe ser O(1). 
    Si se quiere extraer de una posición indebida, que se arroje la debida excepción.
    """
    def extraer(posicion=None):

        #Si la lista está vacía, no se puede extraer ningún elemento
        if self.esta_vacia():
            raise IndexError("La lista está vacía")
        
        #Si no se especifica una posición, se indica el último elemento de la lista
        if posicion == None:
            posicion = self.tamanio - 1
        
        #Valida que la posición sea un número entero dentro del rango válido
        if posicion < 0 or posicion >= self.tamanio or not isinstance(posicion, int):
            raise IndexError("Posición fuera de rango o inválida")
        
        nodo_extraido = self._get_nodo(posicion)
        dato_extraido = nodo_extraido.dato
        
        if nodo_extraido.anterior:
            nodo_extraido.anterior.siguiente = nodo_extraido.siguiente
        else:
            self.cabeza = nodo_extraido.siguiente
        
        if nodo_extraido.siguiente:
            nodo_extraido.siguiente.anterior = nodo_extraido.anterior
        else:
            self.cola = nodo_extraido.anterior
        
        self.tamanio -= 1
        return dato_extraido
    
    # Metodo auxiliar para obtener el nodo en una posición específica,
    # optimizado para acceder desde ambos extremos
    def _get_nodo(self, posicion):
        # Optimización O(n/2)
        if posicion < self.tamanio // 2:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
        else:
            actual = self.cola
            for _ in range(self.tamanio - 1, posicion, -1):
                actual = actual.anterior
        return actual

    """
    copiar(): Realiza una copia de la lista elemento a elemento y devuelve la copia.
    Verificar que el orden de complejidad de este método sea O(n) y no O(n^2).
    """
    def copiar(self):
        nueva_lista = ListaDobleEnlazada()
        actual = self.cabeza
        while actual:
            # agregar_al_final es O(1), por lo que el bucle es O(n)
            nueva_lista.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return nueva_lista

    """
    invertir(): Invierte el orden de los elementos de la lista.
    """
    def invertir(self):

        #Si esta vacía o tiene un solo elemento, no es necesario invertir
        if self.esta_vacia() or self.tamanio == 1:
            return
        
        # Para invertir la lista, se recorren los nodos y se intercambian sus punteros siguiente y anterior    
        actual = self.cabeza
        self.cola = actual 
        temporal = None
        
        # El bucle recorre la lista y va intercambiando los punteros de cada nodo.
        # Al finalizar, el último nodo procesado (temporal) será la nueva cabeza de la lista.
        while actual:
            temporal = actual.anterior
            actual.anterior = actual.siguiente
            actual.siguiente = temporal
            actual = actual.anterior # Se mueve al siguiente original
        
        # Si hay un nodo temporal, se actualiza la cabeza de la lista
        if temporal:
            self.cabeza = temporal.anterior

    """
    concatenar(Lista): Recibe una lista como argumento y retorna la lista actual
    con la lista pasada como parámetro concatenada al final de la primera.
    """
    def concatenar(self, otra_lista):
        # El test espera que se recorra otra_lista y se agregue a la actual
        for item in otra_lista:
            self.agregar_al_final(item)
        return self
    
    """ __len__(): Devuelve el número de ítems de la lista.
    """
    def __len__(self):
        return self.tamanio

    """
    __add__(Lista): El resultado de “sumar” dos listas debería ser una nueva lista 
    con los elementos de la primera lista y los de la segunda.
    Aprovechar el método concatenar para evitar repetir código.
    """
    def __add__(self, otra_lista):
        # Según el test lde_3 + lde_2 no debe modificar las originales
        nueva = self.copiar()
        return nueva.concatenar(otra_lista)
    
    """ __iter__(): permite que la lista sea recorrida con un ciclo for
    """
    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.dato # yield pausa la función y preserva el estado de las variables.
            actual = actual.siguiente