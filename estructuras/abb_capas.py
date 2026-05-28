class NodoCapa:

    def __init__(self, capa):

        self.capa = capa
        self.izquierda = None
        self.derecha = None


class ArbolCapas:

    def __init__(self):

        self.raiz = None


    # ==========================================
    # INSERTAR
    # ==========================================

    def insertar(self, capa):

        self.raiz = self._insertar(
            self.raiz,
            capa
        )

    def _insertar(self, nodo, capa):

        if nodo is None:

            return NodoCapa(capa)

        if capa.id < nodo.capa.id:

            nodo.izquierda = self._insertar(
                nodo.izquierda,
                capa
            )

        else:

            nodo.derecha = self._insertar(
                nodo.derecha,
                capa
            )

        return nodo


    # ==========================================
    # RECORRIDO INORDEN
    # ==========================================

    def inorden(self):

        print("\n======= INORDEN =======")

        self._inorden(self.raiz)

    def _inorden(self, nodo):

        if nodo:

            self._inorden(nodo.izquierda)

            print("Capa:", nodo.capa.id)

            self._inorden(nodo.derecha)


    # ==========================================
    # RECORRIDO PREORDEN
    # ==========================================

    def preorden(self):

        print("\n======= PREORDEN =======")

        self._preorden(self.raiz)

    def _preorden(self, nodo):

        if nodo:

            print("Capa:", nodo.capa.id)

            self._preorden(nodo.izquierda)

            self._preorden(nodo.derecha)


    # ==========================================
    # RECORRIDO POSTORDEN
    # ==========================================

    def postorden(self):

        print("\n======= POSTORDEN =======")

        self._postorden(self.raiz)

    def _postorden(self, nodo):

        if nodo:

            self._postorden(nodo.izquierda)

            self._postorden(nodo.derecha)

            print("Capa:", nodo.capa.id)


    # ==========================================
    # MOSTRAR CAPA
    # ==========================================

    def mostrar_capa(self, id_buscar):

        encontrado = self._mostrar_capa(
            self.raiz,
            id_buscar
        )

        if not encontrado:

            print("Capa no encontrada")


    def _mostrar_capa(self, nodo, id_buscar):

        if nodo is None:

            return False


        # BUSCAR IZQUIERDA
        encontrado = self._mostrar_capa(
            nodo.izquierda,
            id_buscar
        )

        if encontrado:

            return True


        # CAPA ENCONTRADA
        if nodo.capa.id == id_buscar:

            print("\n======= CAPA =======")
            print("ID:", nodo.capa.id)
            print("Cantidad pixeles:", len(nodo.capa.pixeles))

            from PIL import Image, ImageDraw

            imagen = Image.new(
                "RGB",
                (500, 500),
                "#87CEEB"
            )

            draw = ImageDraw.Draw(imagen)

            for pixel in nodo.capa.pixeles:

                draw.point(
                    (
                        pixel.x + 60,
                        pixel.y + 40
                    ),
                    fill=pixel.color
                )

            nombre = "capa_" + str(id_buscar) + ".png"

            imagen.save(nombre)

            print("Imagen generada:", nombre)

            return True


        # BUSCAR DERECHA
        return self._mostrar_capa(
            nodo.derecha,
            id_buscar
        )