from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.listar_posts, name="lista"),
    path("agregar/", views.agregar_post, name="agregar"),
    path("<int:post_id>/", views.detalle_post, name="detalle"),
    path("<int:post_id>/like/", views.dar_like, name="like"),
]
