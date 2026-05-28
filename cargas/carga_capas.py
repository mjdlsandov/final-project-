from modelos.capa import Capa
from modelos.pixel import Pixel

def bloque(capa, x, y, color):

    for i in range(20):

        for j in range(20):

            pixel = Pixel(
                x + i,
                y + j,
                color
            )

            capa.agregar_pixel(pixel)


def cargar_capas(ruta, arbol_capas):

    with open(ruta, "r") as archivo:

        for linea in archivo:

            linea = linea.strip()

            if linea == "":
                continue

            id_capa = int(linea)

            capa = Capa(id_capa)

            # Capa 1. Cara

            if id_capa == 1:

                cara = [

                    "00011111000",
                    "00111111100",
                    "01111111110",
                    "11111111111",
                    "11111111111",
                    "11111111111",
                    "11111111111",
                    "11111111111",
                    "01111111110",
                    "00111111100",
                    "00011111000"

                ]

                for fila in range(len(cara)):

                    for columna in range(len(cara[fila])):

                        if cara[fila][columna] == "1":

                            x = columna * 20 + 100
                            y = fila * 20 + 80

                            bloque(
                                capa,
                                x,
                                y,
                                "#FFFF00"
                            )

            # Capa 2. Ojo izquierdo

            elif id_capa == 2:

                bloque(capa, 160, 180, "#000000")
                bloque(capa, 160, 200, "#000000")

            # Capa 3. Ojo derecho

            elif id_capa == 3:

                bloque(capa, 240, 180, "#000000")
                bloque(capa, 240, 200, "#000000")

            # Capa 4. Boca

            elif id_capa == 4:

                bloque(capa, 160, 240, "#000000")
                bloque(capa, 180, 260, "#000000")
                bloque(capa, 200, 260, "#000000")
                bloque(capa, 220, 260, "#000000")
                bloque(capa, 240, 240, "#000000")

            # Capa 5. Mejias

            elif id_capa == 5:

                bloque(capa, 160, 230, "#FF69B4")
                bloque(capa, 290, 230, "#FF69B4")

            # Insertar capa en el arbol


            arbol_capas.insertar(capa)

            print("Capa cargada:", id_capa)
