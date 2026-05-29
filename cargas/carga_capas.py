from modelos.capa import Capa
from modelos.pixel import Pixel


def cargar_capas(ruta, arbol_capas):

    capa_actual = None

    with open(ruta, "r") as archivo:

        for linea in archivo:

            linea = linea.strip()

            # ignorar vacias
            if linea == "":
                continue

            # inicio capa
            if "{" in linea:

                id_capa = int(
                    linea.replace("{", "")
                )

                capa_actual = Capa(id_capa)

                continue

            # fin capa
            if "}" in linea:

                if capa_actual is not None:

                    arbol_capas.insertar(
                        capa_actual
                    )

                    print(
                        "Capa cargada:",
                        capa_actual.id
                    )

                    capa_actual = None

                continue

            # pixeles
            if capa_actual is not None:

                linea = linea.replace(
                    ";",
                    ""
                )

                datos = linea.split(",")

                if len(datos) != 3:
                    continue

                x = int(datos[0])

                y = int(datos[1])

                color = datos[2].strip()

                pixel = Pixel(
                    x,
                    y,
                    color
                )

                capa_actual.agregar_pixel(
                    pixel
                )