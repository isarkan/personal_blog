class EliminarArticulo:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def ejecutar(self, id):
        self.repositorio.eliminar(id)