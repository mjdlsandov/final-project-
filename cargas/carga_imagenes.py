from modelos.imagen import Imagen


def cargar_imagenes(ruta, lista_imagenes):

    with open(ruta, "r") as archivo:

        for linea in archivo:

            linea = linea.strip()

            if linea:

                id_imagen = linea

                imagen = Imagen(id_imagen)

                lista_imagenes.insertar(imagen)

                print("Imagen cargada:", id_imagen)