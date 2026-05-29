from modelos.usuario import Usuario


def cargar_usuarios(ruta, arbol_usuarios):

    with open(ruta, "r") as archivo:

        for linea in archivo:

            linea = linea.strip()

            if linea == "":
                continue

            linea = linea.replace(";", "")

            nombre, imagenes_texto = linea.split(":")

            usuario = Usuario(nombre)

            if imagenes_texto != "":
                imagenes = imagenes_texto.split(",")

                for imagen in imagenes:
                    usuario.imagenes.append(imagen)

            arbol_usuarios.insertar(usuario)

            print("Usuario cargado:", nombre)