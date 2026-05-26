from modelos.usuario import Usuario


def cargar_usuarios(ruta, arbol_usuarios):

    with open(ruta, "r") as archivo:

        for linea in archivo:

            linea = linea.strip()

            if linea:

                nombre, datos = linea.split(":")

                usuario = Usuario(nombre)

                arbol_usuarios.insertar(usuario)

                print("Usuario cargado:", nombre)