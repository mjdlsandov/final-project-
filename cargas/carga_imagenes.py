def cargar_imagenes(ruta, lista_imagenes):

    with open(ruta, "r") as archivo:

        for linea in archivo:

            linea = linea.strip()

            if linea == "":
                continue

            if "{" in linea and "}" in linea:

                id_imagen = linea.split("{")[0]

                capas_texto = linea.split("{")[1].replace("}", "")

                capas = capas_texto.split(",")

                lista_imagenes.insertar(
                    id_imagen,
                    capas
                )

                print("Imagen cargada:", id_imagen)