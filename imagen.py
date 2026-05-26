class Imagen:

    def __init__(self, id_imagen):
        self.id = id_imagen
        self.capas = []

    def agregar_capa(self, capa):
        self.capas.append(capa)