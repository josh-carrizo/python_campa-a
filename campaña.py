# from video import Video
# from social import Social
# from display import Display
from anuncio import Video, Social, Display
from error import LargoExcedidoError

class Campaña():
    def __init__(self, nombre: str, fecha_inicio: str, fecha_termino: str, anuncios: list = None):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self._anuncios = anuncios if anuncios is not None else []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 250:
            raise LargoExcedidoError("El nombre de la campaña no debe sobrepasar los 250 caracteres.")
        self._nombre = nuevo_nombre

    @property
    def fecha_inicio(self):
        return self._fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self, valor):
        self._fecha_inicio = valor
    
    @property
    def fecha_termino(self):
        return self._fecha_termino
    
    @fecha_termino.setter
    def fecha_termino(self, valor):
        self._fecha_termino = valor
    
    @property
    def anuncios(self):
        return self._anuncios

    def __str__(self):
        count_video = sum(1 for anuncio in self._anuncios if isinstance(anuncio, Video))
        count_display = sum(1 for anuncio in self._anuncios if isinstance(anuncio, Display))
        count_social = sum(1 for anuncio in self._anuncios if isinstance(anuncio, Social))

        return (f"Nombre de la campaña: {self.nombre}\n"
                f"Anuncios: {count_video} Video,\t {count_display} Display,\t {count_social} Social")
