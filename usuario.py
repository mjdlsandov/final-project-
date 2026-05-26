class Usuario:

    def __init__(self, nombre):
        self.nombre = nombre
        self.imagenes = []

    def agregar_imagen(self, imagen):
        self.imagenes.append(imagen)