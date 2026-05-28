from graphviz import Digraph


def graficar_imagen():

    dot = Digraph()

    # Nodo principal
    dot.node(
        "Imagen",
        "Imagen Feliz"
    )

    # Capas
    for i in range(1, 6):

        nombre = "Capa " + str(i)

        dot.node(
            str(i),
            nombre
        )

        dot.edge(
            "Imagen",
            str(i)
        )

    dot.render(
        "grafo_imagen",
        format="png",
        view=True
    )

    print("Grafo imagen generado")