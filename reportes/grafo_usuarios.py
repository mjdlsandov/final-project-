from graphviz import Digraph


def graficar_arbol_usuarios(arbol):

    dot = Digraph("ArbolUsuarios")
    dot.attr(rankdir="TB")
    dot.attr("node", fontname="Arial")

    def recorrer(nodo):

        if nodo is not None:

            usuario_id = "usuario_" + nodo.usuario.nombre

            dot.node(
                usuario_id,
                nodo.usuario.nombre,
                shape="record",
                color="blue"
            )

            if nodo.izquierda is not None:

                izquierda_id = "usuario_" + nodo.izquierda.usuario.nombre

                dot.edge(
                    usuario_id,
                    izquierda_id,
                    color="black"
                )

            if nodo.derecha is not None:

                derecha_id = "usuario_" + nodo.derecha.usuario.nombre

                dot.edge(
                    usuario_id,
                    derecha_id,
                    color="black"
                )

            anterior = usuario_id

            for imagen in nodo.usuario.imagenes:

                imagen_id = (
                    "imagen_" +
                    nodo.usuario.nombre +
                    "_" +
                    str(imagen)
                )

                dot.node(
                    imagen_id,
                    "img" + str(imagen),
                    shape="box",
                    color="red"
                )

                dot.edge(
                    anterior,
                    imagen_id,
                    color="black"
                )

                anterior = imagen_id

            recorrer(nodo.izquierda)
            recorrer(nodo.derecha)

    recorrer(arbol.raiz)

    dot.render(
        "arbol_usuarios",
        format="png",
        cleanup=True
    )

    print("Arbol de usuarios generado")