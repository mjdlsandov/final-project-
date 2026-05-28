from PIL import Image, ImageDraw

# Centrado

OFFSET_X = 60
OFFSET_Y = 40


def dibujar_pixeles(draw, capa, color=None):

    for pixel in capa.pixeles:

        draw.point(
            (
                pixel.x + OFFSET_X,
                pixel.y + OFFSET_Y
            ),
            fill=color if color else pixel.color
        )

# Imagen GENERAL

def generar_imagen_general(arbol_capas):

    imagen = Image.new(
        "RGB",
        (500, 500),
        "#87CEEB"
    )

    draw = ImageDraw.Draw(imagen)

    def recorrer(nodo):

        if nodo:

            dibujar_pixeles(draw, nodo.capa)

            recorrer(nodo.izquierda)

            recorrer(nodo.derecha)

    recorrer(arbol_capas.raiz)

    imagen.save("imagen_general.png")

    print("Imagen GENERAL generada")

# Imagen INORDEN

def generar_imagen(arbol_capas):

    imagen = Image.new(
        "RGB",
        (500, 500),
        "#87CEEB"
    )

    draw = ImageDraw.Draw(imagen)

    def recorrer(nodo):

        if nodo:

            recorrer(nodo.izquierda)

            dibujar_pixeles(draw, nodo.capa)

            recorrer(nodo.derecha)

    recorrer(arbol_capas.raiz)

    imagen.save("imagen_inorden.png")

    print("Imagen INORDEN generada")

# Imagen PREORDEN

def generar_imagen_preorden(arbol_capas):

    imagen = Image.new(
        "RGB",
        (500, 500),
        "#87CEEB"
    )

    draw = ImageDraw.Draw(imagen)

    def recorrer(nodo):

        if nodo:

            dibujar_pixeles(
                draw,
                nodo.capa,
                "blue"
            )

            recorrer(nodo.izquierda)

            recorrer(nodo.derecha)

    recorrer(arbol_capas.raiz)

    imagen.save("imagen_preorden.png")

    print("Imagen PREORDEN generada")

# Imagen POSTORDEN

def generar_imagen_postorden(arbol_capas):

    imagen = Image.new(
        "RGB",
        (500, 500),
        "#87CEEB"
    )

    draw = ImageDraw.Draw(imagen)

    def recorrer(nodo):

        if nodo:

            recorrer(nodo.izquierda)

            recorrer(nodo.derecha)

            dibujar_pixeles(
                draw,
                nodo.capa,
                "red"
            )

    recorrer(arbol_capas.raiz)

    imagen.save("imagen_postorden.png")

    print("Imagen POSTORDEN generada")
