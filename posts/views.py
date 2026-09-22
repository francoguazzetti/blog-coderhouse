from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post


def listar_posts(request):
    """Página principal: todos los posts, más estadísticas rápidas."""
    posts = Post.objects.all()
    contexto = {
        "posts": posts,
        "promedio_likes": Post.promedio_likes(),
        "mas_popular": Post.post_mas_popular(),
    }
    return render(request, "posts/lista.html", contexto)


def detalle_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "posts/detalle.html", {"post": post})


def agregar_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("posts:detalle", post_id=post.id)
    else:
        form = PostForm()
    return render(request, "posts/agregar.html", {"form": form})


def dar_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        post.dar_like()
    return redirect("posts:detalle", post_id=post.id)
