class NodoUsuario:

    def __init__(self, usuario):
        self.usuario = usuario
        self.izquierda = None
        self.derecha = None


class ArbolUsuarios:

    def __init__(self):
        self.raiz = None

    def insertar(self, usuario):
        self.raiz = self._insertar(self.raiz, usuario)

    def _insertar(self, nodo, usuario):

        if nodo is None:
            return NodoUsuario(usuario)

        if usuario.nombre < nodo.usuario.nombre:
            nodo.izquierda = self._insertar(nodo.izquierda, usuario)

        elif usuario.nombre > nodo.usuario.nombre:
            nodo.derecha = self._insertar(nodo.derecha, usuario)

        return nodo