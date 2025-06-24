# Clases importadas de la carpeta 'modelo'
from modelo.genero import Genero
from modelo.base import session

# Crear nuevos géneros de libros
def crear_genero(nombre):
    genero = Genero(nombre=nombre)
    session.add(genero)
    session.commit()
    return genero

# Listar todos los géneros de libros existentes
def listar_generos():
    return session.query(Genero).all()