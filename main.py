from estructuras.abb_capas import ArbolCapas
from estructuras.abb_usuarios import ArbolUsuarios
from estructuras.lista_imagenes import ListaCircularDoble

from cargas.carga_capas import cargar_capas
from cargas.carga_imagenes import cargar_imagenes
from cargas.carga_usuarios import cargar_usuarios

from reportes.graphviz_reportes import graficar_arbol_capas
from reportes.grafo_usuarios import graficar_arbol_usuarios
from reportes.grafo_imagen import graficar_imagen
from reportes.grafo_lista_imagenes import graficar_lista_imagenes
from reportes.estado_memoria import graficar_estado_memoria

from generacion.generador_imagen import (
    generar_imagen_por_usuario
)

from modelos.usuario import Usuario

import os


arbol_capas = ArbolCapas()
arbol_usuarios = ArbolUsuarios()
lista_imagenes = ListaCircularDoble()


while True:

    print("\n========== MENU ==========")
    print("1. Cargar capas")
    print("2. Cargar imagenes")
    print("3. Cargar usuarios")
    print("4. Ver arbol capas")
    print("5. Mostrar capas INORDEN")
    print("6. Mostrar capas PREORDEN")
    print("7. Mostrar capas POSTORDEN")
    print("8. Ver lista de imagenes")
    print("9. Ver capa")
    print("10. Ver imagen y arbol de capas")
    print("11. Ver arbol usuarios")
    print("12. Graficar estado de memoria")
    print("13. Agregar usuario")
    print("14. Ver usuarios")
    print("15. Agregar imagen a usuario")
    print("16. Eliminar imagen de usuario")
    print("17. Generar imagen usuario")
    print("18. Eliminar usuario")
    print("19. Eliminar imagen generada")
    print("20. Salir")

    opcion = input("Seleccione opcion: ")

    if opcion == "1":

        ruta = input("Ruta archivo capas: ")
        cargar_capas(ruta, arbol_capas)

    elif opcion == "2":

        ruta = input("Ruta archivo imagenes: ")
        cargar_imagenes(ruta, lista_imagenes)

    elif opcion == "3":

        ruta = input("Ruta archivo usuarios: ")
        cargar_usuarios(ruta, arbol_usuarios)

    elif opcion == "4":

        graficar_arbol_capas(arbol_capas)

    elif opcion == "5":

        arbol_capas.inorden()

    elif opcion == "6":

        arbol_capas.preorden()

    elif opcion == "7":

        arbol_capas.postorden()

    elif opcion == "8":

        lista_imagenes.mostrar()

        graficar_lista_imagenes(
            lista_imagenes
        )

    elif opcion == "9":

        id_capa = int(
            input("Ingrese ID capa: ")
        )

        arbol_capas.mostrar_capa(
            id_capa
        )

    elif opcion == "10":

        id_imagen = input(
            "Ingrese ID imagen: "
        )

        graficar_imagen(
            lista_imagenes,
            arbol_capas,
            id_imagen
        )

    elif opcion == "11":

        graficar_arbol_usuarios(
            arbol_usuarios
        )

    elif opcion == "12":

        graficar_estado_memoria(
            arbol_capas,
            arbol_usuarios,
            lista_imagenes
        )

    elif opcion == "13":

        nombre = input(
            "Nombre usuario: "
        )

        usuario = Usuario(nombre)

        arbol_usuarios.insertar(
            usuario
        )

        print("Usuario agregado")

    elif opcion == "14":

        arbol_usuarios.inorden()

    elif opcion == "15":

        nombre_usuario = input(
            "Usuario: "
        )

        nombre_imagen = input(
            "Imagen: "
        )

        arbol_usuarios.agregar_imagen_usuario(
            nombre_usuario,
            nombre_imagen
        )

    elif opcion == "16":

        nombre_usuario = input(
            "Usuario: "
        )

        nombre_imagen = input(
            "Imagen: "
        )

        arbol_usuarios.eliminar_imagen_usuario(
            nombre_usuario,
            nombre_imagen
        )

    elif opcion == "17":

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

            generar_imagen_por_usuario(
                lista_imagenes,
                arbol_capas,
                seleccion
            )

        else:

            print("Usuario no encontrado")

    elif opcion == "18":

        nombre = input(
            "Nombre usuario eliminar: "
        )

        arbol_usuarios.eliminar(
            nombre
        )

        print("Usuario eliminado")

    elif opcion == "19":

        nombre = input(
            "Nombre imagen: "
        )

        if os.path.exists(nombre):

            os.remove(nombre)

            print("Imagen eliminada")

        else:

            print("Imagen no encontrada")

    elif opcion == "20":

        print("Saliendo...")
        break

    else:

        print("Opcion invalida")
