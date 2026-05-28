from graphviz import Digraph


def graficar_arbol_capas(arbol):

    # Crear grafo
    dot = Digraph("ArbolCapas")

    # Diseño 
    dot.attr(rankdir='TB')
    dot.attr(
        'node',
        shape='circle',
        style='filled',
        color='lightblue',
        fontname='Arial'
    )

    def recorrer(nodo):

        if nodo is not None:

            # Crear nodo actual
            dot.node(
                str(nodo.capa.id),
                "Capa " + str(nodo.capa.id)
            )

            # Conexión izquierda
            if nodo.izquierda:

                dot.edge(
                    str(nodo.capa.id),
                    str(nodo.izquierda.capa.id)
                )

            # Conexión derecha
            if nodo.derecha:

                dot.edge(
                    str(nodo.capa.id),
                    str(nodo.derecha.capa.id)
                )

            # Recorrer hijos
            recorrer(nodo.izquierda)
            recorrer(nodo.derecha)

    # Empezar recorrido
    recorrer(arbol.raiz)

    # Generar PNG
    dot.render(
        "arbol_capas",
        format="png",
        cleanup=True
    )

    print("Reporte Graphviz generado")