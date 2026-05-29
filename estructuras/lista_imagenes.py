class Imagen:

    def __init__(self, id_imagen, capas):

        self.id = id_imagen
        self.capas = capas


class NodoImagen:

    def __init__(self, imagen):

        self.imagen = imagen
        self.siguiente = None
        self.anterior = None


class ListaCircularDoble:

    def __init__(self):

        self.primero = None


    def insertar(self, id_imagen, capas):

        imagen = Imagen(id_imagen, capas)

        nuevo = NodoImagen(imagen)

        if self.primero is None:

            self.primero = nuevo
            nuevo.siguiente = nuevo
            nuevo.anterior = nuevo

        else:

            ultimo = self.primero.anterior

            ultimo.siguiente = nuevo
            nuevo.anterior = ultimo
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo

        print("Imagen insertada:", id_imagen)


    def mostrar(self):

        if self.primero is None:

            print("No hay imagenes cargadas")
            return

        actual = self.primero

        while True:

            print("Imagen:", actual.imagen.id)
            print("Capas:", actual.imagen.capas)
            print("---------------------")

            actual = actual.siguiente

            if actual == self.primero:
                break


    def buscar(self, id_imagen):

        if self.primero is None:
            return None

        actual = self.primero

        while True:

            if str(actual.imagen.id) == str(id_imagen):
                return actual.imagen

            actual = actual.siguiente

            if actual == self.primero:
                break

        return None