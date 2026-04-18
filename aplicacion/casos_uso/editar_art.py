class EditarArticulo:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def ejecutar(self, id, titulo, contenido):
        articulo = self.repositorio.obtener_por_id(id)
        articulo.editar(titulo, contenido)
        self.repositorio.guardar(articulo)