# Clases importadas de la carpeta 'modelo'
from modelo.usuario import Usuario
from modelo.genero import Genero
from modelo.base import session

# Añadir nuevos usuarios a la base de datos
def crear_usuario(nombre, correo, genero_favorito_id=None):
    usuario = Usuario(nombre=nombre, correo=correo, genero_favorito_id=genero_favorito_id)
    session.add(usuario)
    session.commit()
    return usuario

# Listar todos los usuarios añadidos
def listar_usuarios():
    return session.query(Usuario).all()

# Actualizar correo y genero favorito de un usuario existente
def actualizar_usuario(id_usuario, nuevo_correo=None, nuevo_genero_favorito_id=None):
    usuario = session.get(Usuario, id_usuario)
    if not usuario:
        print(f"No se encontró usuario con id {id_usuario}")
        return None
    
    if nuevo_correo:
        usuario.correo = nuevo_correo
    
    if nuevo_genero_favorito_id is not None:
        genero = session.get(Genero, nuevo_genero_favorito_id)
        if genero:
            usuario.genero_favorito_id = nuevo_genero_favorito_id
        else:
            print(f"No existe genero con id {nuevo_genero_favorito_id}, no se actualizó el género favorito.")
    
    session.commit()
    return usuario