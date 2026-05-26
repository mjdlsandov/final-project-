from graphviz import Digraph


def graficar_arbol_capas(arbol):

    dot = Digraph()

    def recorrer(nodo):

        if nodo is not None:

            dot.node(
                str(nodo.capa.id),
                "Capa " + str(nodo.capa.id)
            )

            if nodo.izquierda:

                dot.edge(
                    str(nodo.capa.id),
                    str(nodo.izquierda.capa.id)
                )

            if nodo.derecha:

                dot.edge(
                    str(nodo.capa.id),
                    str(nodo.derecha.capa.id)
                )

            recorrer(nodo.izquierda)

            recorrer(nodo.derecha)

    recorrer(arbol.raiz)

    dot.render("arbol_capas", format="png")