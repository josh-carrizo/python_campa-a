# from display import Display
# from social import Social
# from video import Video
from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

class Anuncio (ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic:str, sub_tipo:str ):
        if ancho < 0 :
            self.ancho = ancho
        else:
            self.ancho = 1
        if alto < 0 :
            self.alto = alto
        else:
            self.alto = 1
        #url_archivo = "Url1"
        self.url_archivo = url_archivo
        #url_clic = "Url2"
        self.url_clic = url_clic
        #sub_tipo = "Tipo"
        self.sub_tipo = sub_tipo
        
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self,valor):
        self._ancho = valor
    
    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, valor):
        self._alto = valor
    
    @property
    def url_archivo(self):
        return self._url_archivo
    
    @url_archivo.setter
    def url_archivo(self, valor):
        self._url_archivo = valor
    
    @property
    def url_clic(self):
        return self._url_clic
    
    @url_clic.setter
    def url_clic(self, valor):
        self._url_clic = valor
    
    @property
    def sub_tipo(self):
        return self._sub_tipo    
    
    @sub_tipo.setter
    def sub_tipo(self, valor):
        if valor not in self.SUB_TIPOS:
            raise SubTipoInvalidoError(f"Subtipo {valor} no es válido para el tipo {self.FORMATO}.")
        self._sub_tipo = valor
        
    @staticmethod
    def mostrar_formatos():
        formatos = [
            (Video.FORMATO, Video.SUB_TIPOS),
            (Display.FORMATO, Display.SUB_TIPOS),
            (Social.FORMATO, Social.SUB_TIPOS)
        ]
        for formato, subtipos in formatos:
            print(f"FORMATO {formato}:")
            for subtipo in subtipos:
                print(f"- {subtipo}")
                        
    @abstractmethod
    def comprimir_anuncio(self):
        pass
    
    @abstractmethod
    def redimensionar_anuncio(self):
        pass    
    
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
        
class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")
        
class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")        