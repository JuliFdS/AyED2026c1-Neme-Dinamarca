
class NodoAVL:
    def __init__(self, clave, valor):
        self.clave = clave    # Objeto datetime (para comparar)
        self.valor = valor    # Objeto Medicion
        self.izq = None
        self.der = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def _get_altura(self, nodo):
        return nodo.altura if nodo else 0

    def _get_balance(self, nodo):
        return self._get_altura(nodo.izq) - self._get_altura(nodo.der) if nodo else 0

    def _rotar_derecha(self, y):
        x = y.izq
        T2 = x.der
        x.der = y
        y.izq = T2
        y.altura = 1 + max(self._get_altura(y.izq), self._get_altura(y.der))
        x.altura = 1 + max(self._get_altura(x.izq), self._get_altura(x.der))
        return x

    def _rotar_izquierda(self, x):
        y = x.der
        T2 = y.izq
        y.izq = x
        x.der = T2
        x.altura = 1 + max(self._get_altura(x.izq), self._get_altura(x.der))
        y.altura = 1 + max(self._get_altura(y.izq), self._get_altura(y.der))
        return y

    def _rebalancear(self, nodo):
        nodo.altura = 1 + max(self._get_altura(nodo.izq), self._get_altura(nodo.der))
        balance = self._get_balance(nodo)

        if balance > 1:
            if self._get_balance(nodo.izq) < 0:
                nodo.izq = self._rotar_izquierda(nodo.izq)
            return self._rotar_derecha(nodo)
        
        if balance < -1:
            if self._get_balance(nodo.der) > 0:
                nodo.der = self._rotar_derecha(nodo.der)
            return self._rotar_izquierda(nodo)
        
        return nodo

    def insertar(self, clave, valor):
        """
        Inserta un nuevo par clave-valor en el árbol o actualiza el valor si la clave ya existe.

        Precondición:
            - clave: Un objeto que implemente los operadores de comparación (<, >, ==). En este sistema, un objeto datetime.
            - valor: El dato asociado a la clave. En este sistema, un objeto Medicion.
        
        Postcondición:
            - Si la clave no existía, se crea un nuevo nodo con dicha información y el método retorna True.
            - Si la clave ya existía, se reemplaza su valor asociado por el nuevo y el método retorna False.
            - La estructura del árbol mantiene estrictamente el balanceo AVL en todos sus nodos.
        """
        def _insertar_recursivo(nodo, clave, valor):
            if not nodo:
                return True, NodoAVL(clave, valor)
            
            nuevo = False
            if clave < nodo.clave:
                nuevo, nodo.izq = _insertar_recursivo(nodo.izq, clave, valor)
            elif clave > nodo.clave:
                nuevo, nodo.der = _insertar_recursivo(nodo.der, clave, valor)
            else:
                nodo.valor = valor  # Actualización
                return False, nodo

            return nuevo, self._rebalancear(nodo)

        es_nuevo, self.raiz = _insertar_recursivo(self.raiz, clave, valor)
        return es_nuevo

    def buscar(self, clave):
        """
        Busca un nodo en el árbol utilizando su clave única.

        Precondición:
            - clave: Un objeto comparable del mismo tipo que las claves almacenadas en el árbol.
        
        Postcondición:
            - El estado interno del árbol permanece inalterado.
        
        Returns:
            - El objeto 'valor' almacenado en el nodo si la clave es hallada.
            - None si la clave no pertenece al árbol.
        """
        def _buscar_recursivo(nodo, clave):
            if not nodo or nodo.clave == clave:
                return nodo
            if clave < nodo.clave:
                return _buscar_recursivo(nodo.izq, clave)
            return _buscar_recursivo(nodo.der, clave)
        
        nodo_encontrado = _buscar_recursivo(self.raiz, clave)
        return nodo_encontrado.valor if nodo_encontrado else None

    def eliminar(self, clave):
        """
        Elimina el nodo correspondiente a la clave recibida y reestructura el árbol.

        Precondición:
            - clave: Un objeto comparable del mismo tipo que las claves almacenadas.
        
        Postcondición:
            - Si la clave existía, el nodo es removido, el árbol se rebalancea manteniendo la propiedad AVL y retorna True.
            - Si la clave no existía, el estado del árbol no se modifica y retorna False.
        """
        def _min_valor_nodo(nodo):
            actual = nodo
            while actual.izq:
                actual = actual.izq
            return actual

        def _eliminar_recursivo(nodo, clave):
            if not nodo:
                return None
            
            if clave < nodo.clave:
                nodo.izq = _eliminar_recursivo(nodo.izq, clave)
            elif clave > nodo.clave:
                nodo.der = _eliminar_recursivo(nodo.der, clave)
            else:
                if not nodo.izq: return nodo.der
                if not nodo.der: return nodo.izq
                
                temp_sucesor = _min_valor_nodo(nodo.der)
                nodo.clave = temp_sucesor.clave
                nodo.valor = temp_sucesor.valor
                nodo.der = _eliminar_recursivo(nodo.der, temp_sucesor.clave)

            return self._rebalancear(nodo)

        if self.buscar(clave) is not None:
            self.raiz = _eliminar_recursivo(self.raiz, clave)
            return True
        return False

    def obtener_rango(self, c1, c2):
        """
        Realiza un recorrido acotado para recuperar los valores en el intervalo cerrado [c1, c2].

        Precondición:
            - c1, c2: Objetos comparables del mismo tipo que las claves del árbol.
            - Se debe cumplir que c1 <= c2.
        
        Postcondición:
            - El estado interno del árbol permanece inalterado.
        
        Returns:
            - list: Una lista con los objetos 'valor' cuyas claves pertenecen al rango, ordenados de forma ascendente.
        """
        resultados = []
        def _rango_inorder(nodo):
            if not nodo:
                return
            if c1 < nodo.clave:
                _rango_inorder(nodo.izq)
            if c1 <= nodo.clave <= c2:
                resultados.append(nodo.valor)
            if c2 > nodo.clave:
                _rango_inorder(nodo.der)
        
        _rango_inorder(self.raiz)
        return resultados