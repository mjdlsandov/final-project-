from PIL import Image, ImageDraw

ANCHO = 1200
ALTO = 800


def dibujar_pixeles_centrados(draw, pixeles):

    if len(pixeles) == 0:
        print("No hay pixeles para dibujar")
        return

    xs = [pixel.x for pixel in pixeles]
    ys = [pixel.y for pixel in pixeles]

    min_x = min(xs)
    max_x = max(xs)

    min_y = min(ys)
    max_y = max(ys)

    ancho_figura = max_x - min_x
    alto_figura = max_y - min_y

    if ancho_figura == 0:
        ancho_figura = 1

    if alto_figura == 0:
        alto_figura = 1

    escala_x = (ANCHO * 0.85) / ancho_figura
    escala_y = (ALTO * 0.85) / alto_figura

    escala = min(escala_x, escala_y)

    nuevo_ancho = ancho_figura * escala
    nuevo_alto = alto_figura * escala

    offset_x = int((ANCHO - nuevo_ancho) / 2)
    offset_y = int((ALTO - nuevo_alto) / 2)

    for pixel in pixeles:

        nuevo_x = int((pixel.x - min_x) * escala) + offset_x
        nuevo_y = int((pixel.y - min_y) * escala) + offset_y

        if 0 <= nuevo_x < ANCHO and 0 <= nuevo_y < ALTO:

            draw.point(
                (nuevo_x, nuevo_y),
                fill=pixel.color
            )


def obtener_pixeles_inorden(arbol_capas):

    pixeles = []

    def recorrer(nodo):

        if nodo:
            recorrer(nodo.izquierda)
            pixeles.extend(nodo.capa.pixeles)
            recorrer(nodo.derecha)

    recorrer(arbol_capas.raiz)

    return pixeles


def obtener_pixeles_preorden(arbol_capas):

    pixeles = []

    def recorrer(nodo):

        if nodo:
            pixeles.extend(nodo.capa.pixeles)
            recorrer(nodo.izquierda)
            recorrer(nodo.derecha)

    recorrer(arbol_capas.raiz)

    return pixeles


def obtener_pixeles_postorden(arbol_capas):

    pixeles = []

    def recorrer(nodo):

        if nodo:
            recorrer(nodo.izquierda)
            recorrer(nodo.derecha)
            pixeles.extend(nodo.capa.pixeles)

    recorrer(arbol_capas.raiz)

    return pixeles


def generar_imagen(arbol_capas):

    imagen = Image.new(
        "RGBA",
        (ANCHO, ALTO),
        (0, 0, 0, 0)
    )

    draw = ImageDraw.Draw(imagen)

    pixeles = obtener_pixeles_inorden(
        arbol_capas
    )

    dibujar_pixeles_centrados(
        draw,
        pixeles
    )

    imagen.save("imagen_inorden.png")

    print("Imagen INORDEN generada")


def generar_imagen_preorden(arbol_capas):

    imagen = Image.new(
        "RGBA",
        (ANCHO, ALTO),
        (0, 0, 0, 0)
    )

    draw = ImageDraw.Draw(imagen)

    pixeles = obtener_pixeles_preorden(
        arbol_capas
    )

    dibujar_pixeles_centrados(
        draw,
        pixeles
    )

    imagen.save("imagen_preorden.png")

    print("Imagen PREORDEN generada")


def generar_imagen_postorden(arbol_capas):

    imagen = Image.new(
        "RGBA",
        (ANCHO, ALTO),
        (0, 0, 0, 0)
    )

    draw = ImageDraw.Draw(imagen)

    pixeles = obtener_pixeles_postorden(
        arbol_capas
    )

    dibujar_pixeles_centrados(
        draw,
        pixeles
    )

    imagen.save("imagen_postorden.png")

    print("Imagen POSTORDEN generada")


def generar_imagen_por_usuario(lista_imagenes, arbol_capas, id_imagen):

    imagen_usuario = lista_imagenes.buscar(
        id_imagen
    )

    if imagen_usuario is None:

        print("Imagen no encontrada")
        return

    pixeles = []

    for id_capa in imagen_usuario.capas:

        capa = arbol_capas.buscar(
            int(id_capa)
        )

        if capa is not None:

            pixeles.extend(
                capa.pixeles
            )

    imagen = Image.new(
        "RGBA",
        (ANCHO, ALTO),
        (0, 0, 0, 0)
    )

    draw = ImageDraw.Draw(imagen)

    dibujar_pixeles_centrados(
        draw,
        pixeles
    )

    # ROTAR LA IMAGEN
    imagen = imagen.rotate(
        -90,
        expand=True
    )

    nombre_archivo = (
        "imagen_usuario_" +
        str(id_imagen) +
        ".png"
    )

    imagen.save(nombre_archivo)

    print(
        "Imagen generada:",
        nombre_archivo
    )