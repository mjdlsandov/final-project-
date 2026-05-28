class NodoUsuario:

    def __init__(self, usuario):

        self.usuario = usuario
        self.izquierda = None
        self.derecha = None


class ArbolUsuarios:

    def __init__(self):

        self.raiz = None

 # Insertar usuario

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


 # Recorrido inorden

    def inorden(self):

        print("\n======= USUARIOS =======")

        self._inorden(self.raiz)

    def _inorden(self, nodo):

        if nodo:

            self._inorden(nodo.izquierda)

            print("Usuario:", nodo.usuario.nombre)

            if len(nodo.usuario.imagenes) > 0:

                print("Imagenes:")

                for imagen in nodo.usuario.imagenes:

                    print("-", imagen)

            else:

                print("Sin imagenes")

            print()

            self._inorden(nodo.derecha)


 # Buscar usuario

    def buscar(self, nombre):

        return self._buscar(
            self.raiz,
            nombre
        )

    def _buscar(self, nodo, nombre):

        if nodo is None:

            return None

        if nodo.usuario.nombre == nombre:

            return nodo.usuario

        if nombre < nodo.usuario.nombre:

            return self._buscar(
                nodo.izquierda,
                nombre
            )

        return self._buscar(
            nodo.derecha,
            nombre
        )

 # Eliminar usuario

    def eliminar(self, nombre):

        self.raiz = self._eliminar(
            self.raiz,
            nombre
        )

    def _eliminar(self, nodo, nombre):

        if nodo is None:

            return nodo

        if nombre < nodo.usuario.nombre:

            nodo.izquierda = self._eliminar(
                nodo.izquierda,
                nombre
            )

        elif nombre > nodo.usuario.nombre:

            nodo.derecha = self._eliminar(
                nodo.derecha,
                nombre
            )

        else:

            # SIN HIJOS IZQUIERDOS
            if nodo.izquierda is None:

                return nodo.derecha

            # SIN HIJOS DERECHOS
            elif nodo.derecha is None:

                return nodo.izquierda

            # BUSCAR MENOR DERECHA
            temporal = self._minimo(
                nodo.derecha
            )

            nodo.usuario = temporal.usuario

            nodo.derecha = self._eliminar(
                nodo.derecha,
                temporal.usuario.nombre
            )

        return nodo


    def _minimo(self, nodo):

        actual = nodo

        while actual.izquierda is not None:

            actual = actual.izquierda

        return actual

 # Agregar imagen a usuario

    def agregar_imagen_usuario(
        self,
        nombre_usuario,
        nombre_imagen
    ):

        usuario = self.buscar(nombre_usuario)

        if usuario:

            usuario.imagenes.append(
                nombre_imagen
            )

            print("Imagen agregada")

        else:

            print("Usuario no encontrado")

 # Eliminar imagen de usuario

    def eliminar_imagen_usuario(
        self,
        nombre_usuario,
        nombre_imagen
    ):

        usuario = self.buscar(nombre_usuario)

        if usuario:

            if nombre_imagen in usuario.imagenes:

                usuario.imagenes.remove(
                    nombre_imagen
                )

                print("Imagen eliminada")

            else:

                print("Imagen no encontrada")

        else:

            print("Usuario no encontrado")