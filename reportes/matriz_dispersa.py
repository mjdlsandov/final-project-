from graphviz import Digraph


def graficar_matriz_dispersa(capa):

    dot = Digraph("MatrizDispersa")
    dot.attr(rankdir="TB")
    dot.attr("node", shape="box", fontname="Arial", fontsize="10")

    # Limitar nodos para que no sea gigante
    pixeles = capa.pixeles[:40]

    if len(pixeles) == 0:
        print("La capa no tiene pixeles")
        return

    filas = sorted(list(set(pixel.x for pixel in pixeles)))
    columnas = sorted(list(set(pixel.y for pixel in pixeles)))

    dot.node("matriz", "matriz", color="black")

    # Encabezados columnas
    for col in columnas:
        dot.node("col_" + str(col), str(col), color="black")

    # Encabezados filas
    for fila in filas:
        dot.node("fila_" + str(fila), str(fila), color="black")

    # Alinear matriz con columnas
    with dot.subgraph() as s:
        s.attr(rank="same")
        s.node("matriz")
        for col in columnas:
            s.node("col_" + str(col))

    # Conectar encabezados columnas horizontalmente
    anterior = "matriz"

    for col in columnas:
        actual = "col_" + str(col)
        dot.edge(anterior, actual, dir="both")
        anterior = actual

    # Conectar encabezados filas verticalmente
    anterior = "matriz"

    for fila in filas:
        actual = "fila_" + str(fila)
        dot.edge(anterior, actual, dir="both")
        anterior = actual

    # Crear nodos de pixeles
    matriz_nodos = {}

    for pixel in pixeles:
        nombre = "p_" + str(pixel.x) + "_" + str(pixel.y)
        matriz_nodos[(pixel.x, pixel.y)] = nombre

        dot.node(
            nombre,
            pixel.color,
            color="black"
        )

    # Alinear cada fila
    for fila in filas:
        with dot.subgraph() as s:
            s.attr(rank="same")
            s.node("fila_" + str(fila))

            for col in columnas:
                if (fila, col) in matriz_nodos:
                    s.node(matriz_nodos[(fila, col)])

    # Conectar pixeles por fila
    for fila in filas:
        anterior = "fila_" + str(fila)

        for col in columnas:
            if (fila, col) in matriz_nodos:
                actual = matriz_nodos[(fila, col)]
                dot.edge(anterior, actual, dir="both")
                anterior = actual

    # Conectar pixeles por columna
    for col in columnas:
        anterior = "col_" + str(col)

        for fila in filas:
            if (fila, col) in matriz_nodos:
                actual = matriz_nodos[(fila, col)]
                dot.edge(anterior, actual, dir="both")
                anterior = actual

    nombre_archivo = "matriz_dispersa_capa_" + str(capa.id)

    dot.render(
        nombre_archivo,
        format="png",
        cleanup=True
    )

    print("Matriz dispersa generada:", nombre_archivo + ".png")