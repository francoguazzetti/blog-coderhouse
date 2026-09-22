"""La clase Post"""

class PostInvalidoError(Exception):
    """Se lanza cuando los datos de un Post no tienen sentido."""
    pass

class Post:

    def __init__(self, titulo, autor, likes=0):
        self.titulo = titulo
        self.autor = autor
        self.likes = likes

    def __repr__(self):
        return f"Post('{self.titulo}', autor='{self.autor}', likes={self._likes})"

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, valor):
        if valor < 0:
            raise PostInvalidoError(
                f"Los likes no pueden ser negativos (recibido: {valor})"
            )
        self._likes = valor

    def dar_like(self):
        self.likes = self.likes + 1

    def resumen(self):
        return f"{self.titulo} — {self.likes} likes"

    def to_dict(self):
        return {"titulo": self.titulo, "autor": self.autor, "likes": self._likes}

class PostDestacado(Post):

    UMBRAL_LIKES = 100

    def resumen(self):
        return f"⭐ {super().resumen()} ⭐"

    def __repr__(self):
        return f"PostDestacado('{self.titulo}', autor='{self.autor}', likes={self._likes})"