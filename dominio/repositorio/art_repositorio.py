from abc import ABC, abstractmethod

class ArticuloRepositorio(ABC):

    @abstractmethod
    def guardar(self, articulo):
        pass

    @abstractmethod
    def obtener_todos(self):
        pass

    @abstractmethod
    def obtener_por_id(self, id):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass