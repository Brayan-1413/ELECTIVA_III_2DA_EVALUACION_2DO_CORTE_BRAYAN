# Clases importadas de la carpeta 'modelo'
from modelo.libro import Libro
from modelo.base import session

# Añadir nuevos libros a la base de datos
def crear_libro(titulo, autor, anio, genero_id):
    libro = Libro(titulo=titulo, autor=autor, anio_publicacion=anio, genero_id=genero_id)
    session.add(libro)
    session.commit()
    return libro

# Listar todos los libros añadidos
def listar_libros():
    return session.query(Libro).all()

# Eliminar libro
def eliminar_libro(id_libro):
    libro = session.get(Libro, id_libro)  # Cambio aquí
    if not libro:
        print(f"No se encontró libro con id {id_libro}")
        return False
    session.delete(libro)
    session.commit()
    print(f"Libro con id {id_libro} eliminado correctamente.")
    return True