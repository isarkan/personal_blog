class ListarArticulos:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def ejecutar(self):
        return self.repositorio.obtener_todos()