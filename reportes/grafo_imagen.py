from graphviz import Digraph


def graficar_imagen(lista_imagenes, arbol_capas, id_imagen):

    imagen = lista_imagenes.buscar(id_imagen)

    if imagen is None:
        print("Imagen no encontrada")
        return

    dot = Digraph("ImagenYArbolCapas")
    dot.attr(rankdir="TB")
    dot.attr("node", fontname="Arial")

    with dot.subgraph(name="cluster_lista") as lista:
        lista.attr(label="Lista de capas de la imagen", color="red")

        lista.node("imagen", "Imagen " + str(imagen.id), shape="box", color="red")

        anterior = "imagen"

        for id_capa in imagen.capas:
            nodo_lista = "lista_" + str(id_capa)

            lista.node(
                nodo_lista,
                "Capa " + str(id_capa),
                shape="ellipse",
                color="red"
            )

            lista.edge(anterior, nodo_lista, color="red")
            anterior = nodo_lista

    with dot.subgraph(name="cluster_arbol") as arbol:
        arbol.attr(label="ABB de capas", color="black")

        def recorrer(nodo):

            if nodo is not None:
                nodo_arbol = "arbol_" + str(nodo.capa.id)

                arbol.node(
                    nodo_arbol,
                    "Capa " + str(nodo.capa.id),
                    shape="record",
                    color="black"
                )

                if nodo.izquierda:
                    arbol.edge(
                        nodo_arbol,
                        "arbol_" + str(nodo.izquierda.capa.id),
                        color="black"
                    )

                if nodo.derecha:
                    arbol.edge(
                        nodo_arbol,
                        "arbol_" + str(nodo.derecha.capa.id),
                        color="black"
                    )

                recorrer(nodo.izquierda)
                recorrer(nodo.derecha)

        recorrer(arbol_capas.raiz)

    for id_capa in imagen.capas:
        id_capa = str(id_capa)

        if arbol_capas.buscar(int(id_capa)) is not None:
            dot.edge(
                "lista_" + id_capa,
                "arbol_" + id_capa,
                color="red",
                style="bold"
            )

    dot.render(
        "imagen_y_arbol_capas",
        format="png",
        cleanup=True
    )

    print("Grafo imagen y arbol de capas generado")