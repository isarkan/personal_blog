class ArticuloRepositorioMemoria:
    def __init__(self):
        self.articulos = []
        self.id_actual = 1

    def guardar(self, articulo):
        if articulo.id is None:
            articulo.id = self.id_actual
            self.id_actual += 1
            self.articulos.append(articulo)
        else:
            for i, a in enumerate(self.articulos):
                if a.id == articulo.id:
                    self.articulos[i] = articulo

    def obtener_todos(self):
        return self.articulos

    def obtener_por_id(self, id):
        for a in self.articulos:
            if a.id == id:
                return a

    def eliminar(self, id):
        self.articulos = [a for a in self.articulos if a.id != id]