class Capa:

    def __init__(self, id_capa):

        self.id = id_capa
        self.pixeles = []

    def agregar_pixel(self, pixel):

        self.pixeles.append(pixel)