from campaña import Campaña
from error import LargoExcedidoError, SubTipoInvalidoError
from anuncio import Video

if __name__ == "__main__":
    video_test = Video("video.mp4", "http://ejemplo.com", "instream", 10)
    campaña = Campaña("Test1", "2024-09-01", "2024-12-01", [video_test])
    try:
        nuevo_nombre = input("Porfavor ingrese un nuevo nombre para la campaña: ")
        campaña.nombre = nuevo_nombre
        
        nuevo_sub_tipo = input("Por favor ingrese un nuevo subtipo para el anuncio (instream/outstream): ")
        campaña.anuncios[0].sub_tipo = nuevo_sub_tipo

    except (LargoExcedidoError, SubTipoInvalidoError) as e:
        with open("error.log", "a") as error_log:
            error_log.write(str(e) + "\n")
        print(f"Error: {e}")
