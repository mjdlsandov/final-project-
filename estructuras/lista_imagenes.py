class NodoImagen:

    def __init__(self, imagen):
        self.imagen = imagen
        self.siguiente = None
        self.anterior = None


class ListaCircularDoble:

    def __init__(self):
        self.primero = None

    def insertar(self, imagen):

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

    def mostrar(self):

        if self.primero is None:
            return

        actual = self.primero

        while True:

            print(actual.imagen.id)

            actual = actual.siguiente

            if actual == self.primero:
                break