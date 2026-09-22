from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "likes", "es_destacado", "creado")
    list_filter = ("autor",)
    search_fields = ("titulo", "autor")
