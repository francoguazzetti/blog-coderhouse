"""Lógica pura del blog: nada de print(), nada de input(). Solo cálculos."""


def buscar_post_por_titulo(posts, titulo):
    for post in posts:
        if post["titulo"] == titulo:
            return post
    return None


def filtrar_posts_por_autor(posts, autor):
    resultado = []
    for post in posts:
        if post["autor"] == autor:
            resultado.append(post)
    return resultado


def promedio_likes(posts):
    total = 0
    for post in posts:
        total += post["likes"]
    return total / len(posts)


def post_mas_popular(posts):
    mas_popular = posts[0]
    for post in posts:
        if post["likes"] > mas_popular["likes"]:
            mas_popular = post
    return mas_popular


def convertir_likes(entrada):
    """Intenta convertir a entero. Devuelve (valor, mensaje_error)."""
    try:
        return int(entrada), None
    except ValueError:
        return 0, "Eso no es un número. Se guardó como 0."
