from dominio.entidades.articulo import Articulo

class CrearArticulo:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def ejecutar(self, titulo, contenido):
        articulo = Articulo(None, titulo, contenido)
        self.repositorio.guardar(articulo)