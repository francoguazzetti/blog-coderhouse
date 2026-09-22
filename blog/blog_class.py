"""La clase Blog: encapsula la lista de posts y decide, al cargar cada fila de la BD, que clase de Post instanciar."""
from blog.almacenamiento import DataBase
from blog.post import Post, PostDestacado


class Blog:
    def __init__(self):
        self.db = DataBase()
        self.posts = self._cargar_posts()

    def _crear_post(self, fila):
        """Creacion de posteos"""
        if fila["likes"] >= PostDestacado.UMBRAL_LIKES:
            return PostDestacado(fila["titulo"], fila["autor"], fila["likes"])
        return Post(fila["titulo"], fila["autor"], fila["likes"])

    def _filas_a_posts(self, filas):
        posts = []
        for fila in filas:
            posts.append(self._crear_post(fila))
        return posts

    def _cargar_posts(self):
        filas = self.db.cargar_posts()
        return self._filas_a_posts(filas)

    def agregar_post(self, titulo, autor, likes):
        Post(titulo, autor, likes)
        self.db.guardar_post(titulo, autor, likes)
        self.post = self._cargar_posts()

    def buscar_post(self, titulo):
        filas = self.db.buscar_post_por_titulo(titulo)
        if filas is None:
            return None
        return self._filas_a_posts(filas)
 
    def filtrar_por_autor(self, autor):
        filas = self.db.filtrar_posts_por_autor(autor)
        return self._filas_a_posts(filas)
 
    def promedio_likes(self):
        total = 0
        for post in self.posts:
            total += post.likes
        return total / len(self.posts)
 
    def post_mas_popular(self):
        mas_popular = self.posts[0]
        for post in self.posts:
            if post.likes > mas_popular.likes:
                mas_popular = post
        return mas_popular