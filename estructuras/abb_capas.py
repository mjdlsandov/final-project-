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

        elif capa.id > nodo.capa.id:

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
    # BUSCAR CAPA
    # ==========================================

    def buscar(self, id_buscar):

        return self._buscar(
            self.raiz,
            id_buscar
        )

    def _buscar(self, nodo, id_buscar):

        if nodo is None:

            return None

        if nodo.capa.id == id_buscar:

            return nodo.capa

        if id_buscar < nodo.capa.id:

            return self._buscar(
                nodo.izquierda,
                id_buscar
            )

        return self._buscar(
            nodo.derecha,
            id_buscar
        )


    # ==========================================
    # MOSTRAR CAPA + MATRIZ DISPERSA
    # ==========================================

    def mostrar_capa(self, id_buscar):

        capa = self.buscar(id_buscar)

        if capa is None:

            print("Capa no encontrada")

            return

        print("\n======= CAPA =======")
        print("ID:", capa.id)
        print("Cantidad pixeles:", len(capa.pixeles))

        # Mostrar algunos pixeles en consola
        print("\nPrimeros pixeles:")

        contador = 0

        for pixel in capa.pixeles:

            print(
                "X:",
                pixel.x,
                "Y:",
                pixel.y,
                "COLOR:",
                pixel.color
            )

            contador += 1

            if contador == 20:
                break

        # Generar imagen individual de la capa
        self.generar_imagen_capa(capa)

        # Generar matriz dispersa con Graphviz
        from reportes.matriz_dispersa import graficar_matriz_dispersa

        graficar_matriz_dispersa(capa)


    # ==========================================
    # GENERAR IMAGEN DE UNA CAPA
    # ==========================================

    def generar_imagen_capa(self, capa):

        from PIL import Image, ImageDraw

        imagen = Image.new(
            "RGB",
            (500, 500),
            "#87CEEB"
        )

        draw = ImageDraw.Draw(imagen)

        for pixel in capa.pixeles:

            draw.point(
                (
                    pixel.x + 60,
                    pixel.y + 40
                ),
                fill=pixel.color
            )

        nombre = "capa_" + str(capa.id) + ".png"

        imagen.save(nombre)

        print("Imagen de capa generada:", nombre)