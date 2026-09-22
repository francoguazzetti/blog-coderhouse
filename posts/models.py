from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


class Post(models.Model):
    """Post del blog.

    Reemplaza a la clase Post/PostDestacado y a la persistencia manual con
    SQLite (blog/post.py, blog/blog_class.py, blog/almacenamiento.py):
    ahora los datos viven en el ORM de Django y "destacado" es una
    propiedad calculada en vez de una subclase aparte.
    """

    UMBRAL_LIKES = 100

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    likes = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creado"]

    def __str__(self):
        return self.resumen()

    def clean(self):
        if self.likes < 0:
            raise ValidationError(
                f"Los likes no pueden ser negativos (recibido: {self.likes})"
            )

    @property
    def es_destacado(self):
        return self.likes >= self.UMBRAL_LIKES

    def dar_like(self):
        self.likes += 1
        self.save(update_fields=["likes"])

    def resumen(self):
        texto = f"{self.titulo} — {self.likes} likes"
        if self.es_destacado:
            return f"⭐ {texto} ⭐"
        return texto

    @classmethod
    def promedio_likes(cls):
        posts = cls.objects.all()
        if not posts:
            return 0
        total = sum(post.likes for post in posts)
        return total / len(posts)

    @classmethod
    def post_mas_popular(cls):
        return cls.objects.order_by("-likes").first()

    @classmethod
    def filtrar_por_autor(cls, autor):
        return cls.objects.filter(autor=autor)

    @classmethod
    def buscar_por_titulo(cls, titulo):
        return cls.objects.filter(titulo=titulo)
