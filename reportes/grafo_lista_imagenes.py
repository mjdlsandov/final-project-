from graphviz import Digraph


def graficar_lista_imagenes(lista_imagenes):

    dot = Digraph("ListaImagenes")
    dot.attr(rankdir="LR")
    dot.attr("node", fontname="Arial")

    if lista_imagenes.primero is None:
        print("No hay imagenes cargadas")
        return

    actual = lista_imagenes.primero

    while True:

        imagen_id = "imagen_" + str(actual.imagen.id)

        dot.node(
            imagen_id,
            "Imagen " + str(actual.imagen.id),
            shape="box",
            color="red"
        )

        # Enlace doble con siguiente imagen
        siguiente_id = "imagen_" + str(actual.siguiente.imagen.id)

        if actual.siguiente != lista_imagenes.primero:

            dot.edge(
                imagen_id,
                siguiente_id,
                dir="both",
                color="red"
            )

        # Lista de capas de cada imagen
        anterior = imagen_id

        for capa in actual.imagen.capas:

            capa_id = (
                "imagen_" +
                str(actual.imagen.id) +
                "_capa_" +
                str(capa)
            )

            dot.node(
                capa_id,
                "Capa " + str(capa),
                shape="ellipse",
                color="blue"
            )

            dot.edge(
                anterior,
                capa_id,
                color="blue"
            )

            anterior = capa_id

        actual = actual.siguiente

        if actual == lista_imagenes.primero:
            break

    # cerrar ciclo visual
    if lista_imagenes.primero.siguiente != lista_imagenes.primero:

        ultimo = lista_imagenes.primero.anterior

        dot.edge(
            "imagen_" + str(ultimo.imagen.id),
            "imagen_" + str(lista_imagenes.primero.imagen.id),
            dir="both",
            color="red"
        )

    dot.render(
        "lista_imagenes",
        format="png",
        cleanup=True
    )

    print("Grafo lista de imagenes generado")