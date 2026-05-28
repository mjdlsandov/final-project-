from estructuras.abb_capas import ArbolCapas
from estructuras.abb_usuarios import ArbolUsuarios
from estructuras.lista_imagenes import ListaCircularDoble

from cargas.carga_capas import cargar_capas
from cargas.carga_imagenes import cargar_imagenes
from cargas.carga_usuarios import cargar_usuarios

from reportes.graphviz_reportes import graficar_arbol_capas
from reportes.grafo_usuarios import graficar_arbol_usuarios
from reportes.grafo_imagen import graficar_imagen

from generacion.generador_imagen import (
    generar_imagen_general,
    generar_imagen,
    generar_imagen_preorden,
    generar_imagen_postorden
)

from modelos.usuario import Usuario

# Estructuras de datos

arbol_capas = ArbolCapas()

arbol_usuarios = ArbolUsuarios()

lista_imagenes = ListaCircularDoble()

# Menu principal

while True:

    print("\n========== MENU ==========")
    print("1. Cargar capas")
    print("2. Cargar imagenes")
    print("3. Cargar usuarios")
    print("4. Ver arbol capas")
    print("5. Generar imagen GENERAL")
    print("6. Generar imagen INORDEN")
    print("7. Generar imagen PREORDEN")
    print("8. Generar imagen POSTORDEN")
    print("9. Mostrar imagenes")
    print("10. Mostrar capas INORDEN")
    print("11. Mostrar capas PREORDEN")
    print("12. Mostrar capas POSTORDEN")
    print("13. Ver capa")
    print("14. Agregar usuario")
    print("15. Ver usuarios")
    print("16. Ver arbol usuarios")
    print("17. Eliminar imagen generada")
    print("18. Ver grafo imagen")
    print("19. Agregar imagen a usuario")
    print("20. Eliminar imagen de usuario")
    print("21. Generar imagen usuario")
    print("22. Eliminar usuario")
    print("23. Salir")

    opcion = input("Seleccione opcion: ")

# Cargar capas

    if opcion == "1":

        ruta = input("Ruta archivo capas: ")

        cargar_capas(
            ruta,
            arbol_capas
        )

# Cargar imagenes

    elif opcion == "2":

        ruta = input("Ruta archivo imagenes: ")

        cargar_imagenes(
            ruta,
            lista_imagenes
        )

# Cargar usuarios

    elif opcion == "3":

        ruta = input("Ruta archivo usuarios: ")

        cargar_usuarios(
            ruta,
            arbol_usuarios
        )

    # Ver arbol capas

    elif opcion == "4":

        graficar_arbol_capas(
            arbol_capas
        )

        print("Reporte generado")

# Generar imagen general

    elif opcion == "5":

        generar_imagen_general(
            arbol_capas
        )

# Generar imagen inorden

    elif opcion == "6":

        generar_imagen(
            arbol_capas
        )

    # Generar imagen preorden

    elif opcion == "7":

        generar_imagen_preorden(
            arbol_capas
        )

    # Generar imagen postorden

    elif opcion == "8":

        generar_imagen_postorden(
            arbol_capas
        )

    # Mostrar imagenes

    elif opcion == "9":

        lista_imagenes.mostrar()

# Mostrar capas inorden

    elif opcion == "10":

        arbol_capas.inorden()

# Mostrar capas preorden

    elif opcion == "11":

        arbol_capas.preorden()

# Mostrar capas postorden

    elif opcion == "12":

        arbol_capas.postorden()

    # Ver capa

    elif opcion == "13":

        id_capa = int(
            input("Ingrese ID capa: ")
        )

        arbol_capas.mostrar_capa(
            id_capa
        )

    # Agregar usuario

    elif opcion == "14":

        nombre = input(
            "Nombre usuario: "
        )

        usuario = Usuario(nombre)

        arbol_usuarios.insertar(
            usuario
        )

        print("Usuario agregado")

    # Ver usuarios

    elif opcion == "15":

        arbol_usuarios.inorden()

# Ver arbol usuarios

    elif opcion == "16":

        graficar_arbol_usuarios(
            arbol_usuarios
        )

        print("Arbol usuarios generado")

    # Eliminar imagen generada

    elif opcion == "17":

        import os

        nombre = input(
            "Nombre imagen: "
        )

        if os.path.exists(nombre):

            os.remove(nombre)

            print("Imagen eliminada")

        else:

            print("Imagen no encontrada")

# Grafo imagen

    elif opcion == "18":

        graficar_imagen(
            arbol_capas
        )

        print("Grafo imagen generado")

# Agregar imagen a usuario

    elif opcion == "19":

        nombre_usuario = input(
            "Usuario: "
        )

        nombre_imagen = input(
            "Nombre imagen: "
        )

        arbol_usuarios.agregar_imagen_usuario(
            nombre_usuario,
            nombre_imagen
        )

# Eliminar imagen de usuario

    elif opcion == "20":

        nombre_usuario = input(
            "Usuario: "
        )

        nombre_imagen = input(
            "Nombre imagen: "
        )

        arbol_usuarios.eliminar_imagen_usuario(
            nombre_usuario,
            nombre_imagen
        )

# Generar imagen usuario

    elif opcion == "21":

        nombre_usuario = input(
            "Usuario: "
        )

        usuario = arbol_usuarios.buscar(
            nombre_usuario
        )

        if usuario:

            print("\nImagenes usuario:")

            for imagen in usuario.imagenes:

                print("-", imagen)

            seleccion = input(
                "Seleccione imagen: "
            )

            if seleccion in usuario.imagenes:

                generar_imagen_general(
                    arbol_capas
                )

                print(
                    "Imagen generada para usuario"
                )

            else:

                print("Imagen no encontrada")

        else:

            print("Usuario no encontrado")

# Eliminar usuario

    elif opcion == "22":

        nombre = input(
            "Nombre usuario eliminar: "
        )

        arbol_usuarios.eliminar(
            nombre
        )

        print("Usuario eliminado")

# Salir

    elif opcion == "23":

        print("Saliendo...")

        break

    else:

        print("Opcion invalida")
