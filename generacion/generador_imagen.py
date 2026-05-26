from PIL import Image


def generar_imagen():

    img = Image.new("RGB", (200, 200), "white")

    pixels = img.load()

    pixels[50, 50] = (255, 0, 0)

    pixels[51, 50] = (255, 0, 0)

    pixels[52, 50] = (255, 0, 0)

    img.save("imagen_generada.png")

    print("Imagen generada")