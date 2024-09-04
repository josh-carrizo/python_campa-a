from anuncio import Anuncio

class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, url_archivo, url_clic, sub_tipo, duracion):
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        if duracion > 0:
            self.duracion = duracion 
        else:
            self.duracion = 5

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")