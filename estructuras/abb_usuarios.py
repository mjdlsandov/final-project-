class NodoUsuario:

    def __init__(self, usuario):

        self.usuario = usuario
        self.izquierda = None
        self.derecha = None


class ArbolUsuarios:

    def __init__(self):

        self.raiz = None

    def insertar(self, usuario):

        self.raiz = self._insertar(
            self.raiz,
            usuario
        )

    def _insertar(self, nodo, usuario):

        if nodo is None:

            return NodoUsuario(usuario)

        if usuario.nombre < nodo.usuario.nombre:

            nodo.izquierda = self._insertar(
                nodo.izquierda,
                usuario
            )

        else:

            nodo.derecha = self._insertar(
                nodo.derecha,
                usuario
            )

        return nodo

    def inorden(self):

        self._inorden(self.raiz)

    def _inorden(self, nodo):

        if nodo:

            self._inorden(nodo.izquierda)

            print("Usuario:", nodo.usuario.nombre)

            self._inorden(nodo.derecha)