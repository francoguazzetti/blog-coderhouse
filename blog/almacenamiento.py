"""
Persistencia con SQLite: reemplaza al archivo de texto (posts.txt) de la
clase anterior por una base de datos relacional real, embebida en un solo
archivo (blog.db). Cero servidor, cero instalación extra: sqlite3 viene
incluido en Python.
"""
import sqlite3
from pathlib import Path

RUTA_DB = Path(__file__).parent.parent / "data" / "blog.db"

class DataBase:

    def __init__(self, path=RUTA_DB):
        self.path = path

    def conectar(self):
        """Abre la conexión y garantiza que la tabla exista, siempre.
        Así ningún otro archivo necesita acordarse de 'crear la tabla' antes de usarla."""
        self.path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(self.path)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                likes INTEGER NOT NULL
            )
        """)
        conn.commit()
        return conn


    def guardar_post(self, titulo, autor, likes):
        """Inserta UN post nuevo. A diferencia del archivo de texto, no se
        reescribe todo: solo se agrega la fila nueva."""
        conn = self.conectar()
        conn.execute(
            "INSERT INTO posts (titulo, autor, likes) VALUES (?, ?, ?)",
            (titulo, autor, likes),
        )
        conn.commit()
        conn.close()


    def cargar_posts(self):
        """Devuelve todos los posts guardados, como una lista de diccionarios
        (la misma forma que devolvía la versión con archivo de texto)."""
        conn = self.conectar()
        filas = conn.execute("SELECT titulo, autor, likes FROM posts").fetchall()
        conn.close()
        return [{"titulo": t, "autor": a, "likes": l} for t, a, l in filas]


    def buscar_post_por_titulo(self, titulo):
        """Alternativa a logica.buscar_post_por_titulo: en vez de recorrer una
        lista en Python, se lo delega a la base de datos con WHERE.
        No la usamos en main.py todavía, pero queda disponible."""
        conn = self.conectar()
        fila = conn.execute(
            "SELECT titulo, autor, likes FROM posts WHERE titulo = ?", (titulo,)
        ).fetchone()
        conn.close()
        if fila:
            return {"titulo": fila[0], "autor": fila[1], "likes": fila[2]}
        return None


    def filtrar_posts_por_autor(self, autor):
        """Alternativa a logica.filtrar_posts_por_autor, resuelta con SQL."""
        conn = self.conectar()
        filas = conn.execute(
            "SELECT titulo, autor, likes FROM posts WHERE autor = ?", (autor,)
        ).fetchall()
        conn.close()
        return [{"titulo": t, "autor": a, "likes": l} for t, a, l in filas]
