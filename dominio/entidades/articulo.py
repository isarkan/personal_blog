# dominio/entidades/articulo.py

from datetime import datetime

class Articulo:
    def __init__(self, id, titulo, contenido, fecha_publicacion=None):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion or datetime.now()

    def editar(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido