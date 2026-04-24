class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    @property
    def cabeza(self):
        return self.primero

    @property
    def cola(self):
        return self.ultimo

    def esta_vacia(self):
        return self.tamanio == 0

    def __len__(self):
        return self.tamanio

    def __iter__(self):
        nodo = self.cabeza
        while nodo is not None:
            yield nodo.dato
            nodo = nodo.siguiente

    def agregar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo
        self.tamanio += 1

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo
            self.ultimo = nuevo_nodo
        self.tamanio += 1

    def copiar(self):
        copia = ListaDobleEnlazada()
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            copia.agregar_al_final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return copia
