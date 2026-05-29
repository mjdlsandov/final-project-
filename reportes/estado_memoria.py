from graphviz import Digraph


def graficar_estado_memoria(arbol_capas, arbol_usuarios, lista_imagenes):

    dot = Digraph("EstadoMemoria")
    dot.attr(rankdir="TB")
    dot.attr("node", fontname="Arial")

    dot.node(
        "memoria",
        "Estado de la memoria",
        shape="box",
        style="filled",
        color="lightgreen"
    )

    dot.node("capas", "ABB de Capas", shape="box", color="blue")
    dot.node("usuarios", "ABB de Usuarios", shape="box", color="blue")
    dot.node("imagenes", "Lista Circular de Imagenes", shape="box", color="blue")

    dot.edge("memoria", "capas")
    dot.edge("memoria", "usuarios")
    dot.edge("memoria", "imagenes")

    # Contar capas
    contador_capas = [0]

    def recorrer_capas(nodo):
        if nodo:
            contador_capas[0] += 1
            recorrer_capas(nodo.izquierda)
            recorrer_capas(nodo.derecha)

    recorrer_capas(arbol_capas.raiz)

    dot.node(
        "total_capas",
        "Capas cargadas: " + str(contador_capas[0]),
        shape="ellipse"
    )

    dot.edge("capas", "total_capas")

    # Contar usuarios
    contador_usuarios = [0]

    def recorrer_usuarios(nodo):
        if nodo:
            contador_usuarios[0] += 1
            recorrer_usuarios(nodo.izquierda)
            recorrer_usuarios(nodo.derecha)

    recorrer_usuarios(arbol_usuarios.raiz)

    dot.node(
        "total_usuarios",
        "Usuarios cargados: " + str(contador_usuarios[0]),
        shape="ellipse"
    )

    dot.edge("usuarios", "total_usuarios")

    # Contar imágenes
    contador_imagenes = 0

    if lista_imagenes.primero is not None:

        actual = lista_imagenes.primero

        while True:

            contador_imagenes += 1

            actual = actual.siguiente

            if actual == lista_imagenes.primero:
                break

    dot.node(
        "total_imagenes",
        "Imagenes cargadas: " + str(contador_imagenes),
        shape="ellipse"
    )

    dot.edge("imagenes", "total_imagenes")

    dot.render(
        "estado_memoria",
        format="png",
        cleanup=True
    )

    print("Estado de memoria generado")