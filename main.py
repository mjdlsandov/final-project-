from estructuras.abb_capas import ArbolCapas
from estructuras.abb_usuarios import ArbolUsuarios
from estructuras.lista_imagenes import ListaCircularDoble

from cargas.carga_capas import cargar_capas
from cargas.carga_imagenes import cargar_imagenes
from cargas.carga_usuarios import cargar_usuarios

from reportes.graphviz_reportes import graficar_arbol_capas

from generacion.generador_imagen import generar_imagen


arbol_capas = ArbolCapas()

arbol_usuarios = ArbolUsuarios()

lista_imagenes = ListaCircularDoble()


while True:

    print("\n--- MENU ---")
    print("1. Cargar capas")
    print("2. Cargar imagenes")
    print("3. Cargar usuarios")
    print("4. Ver arbol capas")
    print("5. Generar imagen")
    print("6. Salir")

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

        print("Reporte generado")

    elif opcion == "5":

        generar_imagen()

    elif opcion == "6":

        break