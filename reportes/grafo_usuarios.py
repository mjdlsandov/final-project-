from graphviz import Digraph


def graficar_arbol_usuarios(arbol):

    dot = Digraph()

    def recorrer(nodo):

        if nodo is not None:

            dot.node(
                nodo.usuario.nombre,
                nodo.usuario.nombre
            )

            if nodo.izquierda:

                dot.edge(
                    nodo.usuario.nombre,
                    nodo.izquierda.usuario.nombre
                )

            if nodo.derecha:

                dot.edge(
                    nodo.usuario.nombre,
                    nodo.derecha.usuario.nombre
                )

            recorrer(nodo.izquierda)

            recorrer(nodo.derecha)

    recorrer(arbol.raiz)

    dot.render(
        "arbol_usuarios",
        format="png",
        view=True
    )

    print("Arbol usuarios generado")