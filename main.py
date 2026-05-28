from estructuras.abb_capas import ArbolCapas
from estructuras.abb_usuarios import ArbolUsuarios
from estructuras.lista_imagenes import ListaCircularDoble

from cargas.carga_capas import cargar_capas
from cargas.carga_imagenes import cargar_imagenes
from cargas.carga_usuarios import cargar_usuarios

from reportes.graphviz_reportes import graficar_arbol_capas
from reportes.grafo_imagen import graficar_imagen
from reportes.grafo_usuarios import graficar_arbol_usuarios

from generacion.generador_imagen import (
    generar_imagen_general,
    generar_imagen,
    generar_imagen_preorden,
    generar_imagen_postorden
)

from modelos.usuario import Usuario

import os

    # Estructuras de datos

arbol_capas = ArbolCapas()

arbol_usuarios = ArbolUsuarios()

lista_imagenes = ListaCircularDoble()

    # Menú

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

    print("19. Salir")

    opcion = input("Seleccione opcion: ")

    # Cargar capas

    if opcion == "1":

        ruta = input("Ruta archivo capas: ")

        cargar_capas(ruta, arbol_capas)

    # Cargar imagenes

    elif opcion == "2":

        ruta = input("Ruta archivo imagenes: ")

        cargar_imagenes(ruta, lista_imagenes)

    # Cargar usuarios

    elif opcion == "3":

        ruta = input("Ruta archivo usuarios: ")

        cargar_usuarios(ruta, arbol_usuarios)

    # Ver arbol capas

    elif opcion == "4":

        graficar_arbol_capas(arbol_capas)

        print("Arbol capas generado")

    # Imagen general

    elif opcion == "5":

        generar_imagen_general(arbol_capas)

    # Imagen en inorden

    elif opcion == "6":

        generar_imagen(arbol_capas)

    # Imagen en preorden

    elif opcion == "7":

        generar_imagen_preorden(arbol_capas)

    # Imagen en postorden

    elif opcion == "8":

        generar_imagen_postorden(arbol_capas)

    # Mostrar imagenes

    elif opcion == "9":

        lista_imagenes.mostrar()

    # INORDEN

    elif opcion == "10":

        arbol_capas.inorden()

    # PREORDEN

    elif opcion == "11":

        arbol_capas.preorden()

    # POSTORDEN

    elif opcion == "12":

        arbol_capas.postorden()

    # Ver capa

    elif opcion == "13":

        id_capa = int(input("Ingrese ID capa: "))

        arbol_capas.mostrar_capa(id_capa)

    # Añadir usuario

    elif opcion == "14":

        nombre = input("Ingrese nombre usuario: ")

        usuario = Usuario(nombre)

        arbol_usuarios.insertar(usuario)

        print("Usuario agregado")

    # Ver usuarios

    elif opcion == "15":

        arbol_usuarios.inorden()

    # Vista a arbol de usuarios

    elif opcion == "16":

        graficar_arbol_usuarios(arbol_usuarios)


    # Eliminar imagenes generadas

    elif opcion == "17":

        archivos = [
            "imagen_general.png",
            "imagen_inorden.png",
            "imagen_preorden.png",
            "imagen_postorden.png"
        ]

        eliminada = False

        for archivo in archivos:

            if os.path.exists(archivo):

                os.remove(archivo)

                eliminada = True

        if eliminada:

            print("Imagenes eliminadas")

        else:

            print("No existen imagenes")

    # Grafo 

    elif opcion == "18":

        graficar_imagen()

    # Salida

    elif opcion == "19":

        print("Saliendo del sistema...")

        break

    else:

        print("Opcion invalida")
