class NodoABB:

    def __init__(self, capa):
        self.capa = capa
        self.izquierda = None
        self.derecha = None


class ArbolCapas:

    def __init__(self):
        self.raiz = None

    def insertar(self, capa):
        self.raiz = self._insertar(self.raiz, capa)

    def _insertar(self, nodo, capa):

        if nodo is None:
            return NodoABB(capa)

        if capa.id < nodo.capa.id:
            nodo.izquierda = self._insertar(nodo.izquierda, capa)

        elif capa.id > nodo.capa.id:
            nodo.derecha = self._insertar(nodo.derecha, capa)

        return nodo

    def inorden(self):
        self._inorden(self.raiz)

    def _inorden(self, nodo):

        if nodo:

            self._inorden(nodo.izquierda)

            print(nodo.capa.id)

            self._inorden(nodo.derecha)