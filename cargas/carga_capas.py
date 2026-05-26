from modelos.capa import Capa


def cargar_capas(ruta, arbol_capas):

    with open(ruta, "r") as archivo:

        for linea in archivo:

            linea = linea.strip()

            if linea:

                id_capa = int(linea)

                capa = Capa(id_capa)

                arbol_capas.insertar(capa)

                print("Capa cargada:", id_capa)