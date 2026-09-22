"""Punto de entrada del programa: el menú, la interfaz con el usuario."""
from blog.blog_class import Blog
from blog.post import PostInvalidoError

def convertir_likes(entrada):
    """Intenta convertir a entero. Devuelve (valor, mensaje_error)."""
    try:
        return int(entrada), None
    except ValueError:
        return 0, "Eso no es un número. Se guardó como 0."
    

def mostrar_estadisticas(blog):
    if not blog.posts:
        print("Todavía no hay posts para calcular estadísticas.")
        return
    try:
        print(f"Promedio de likes: {blog.promedio_likes():.1f}")
        print(f"Más popular: {blog.post_mas_popular().titulo}")
    except (ZeroDivisionError, IndexError):
        print("Todavía no hay posts para calcular estadísticas.")


def gestor_blog():
    blog = Blog()
    print(f"Se cargaron {len(blog.posts)} posts guardados.")

    while True:
        print("\n=== GESTOR DE BLOG ===")
        print("1.Agregar 2.Listar 3.Buscar")
        print("4.Filtrar 5.Stats 6.Salir")
        opcion = input("Elegí: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            likes, error = convertir_likes(input("Likes: "))
            if error:
                print(error)
            try:
                blog.agregar_post(titulo, autor, likes)
                print("Post agregado y guardado en la base de datos.")
            except PostInvalidoError as e:
                print(f"No se pudo agregar el post: {e}")

        elif opcion == "2":
            if not blog.posts:
                print("Todavía no hay posts.")
            for post in blog.posts:
                print("-", post.resumen())

        elif opcion == "3":
            titulo = input("Título a buscar: ")
            resultado = blog.buscar_post(titulo)
            print(resultado if resultado else "No se encontró ese post.")

        elif opcion == "4":
            autor = input("Autor a filtrar: ")
            resultados = blog.filtrar_por_autor(autor)
            if not resultados:
                print("Ese autor no tiene posts.")
            for post in resultados:
                print("-", post.resumen())
 
        elif opcion == "5":
            mostrar_estadisticas(blog)
 
        elif opcion == "6":
            print("¡Hasta la próxima!")
            break
 
        else:
            print("Opción inválida.")
 
 
if __name__ == "__main__":
    gestor_blog()
