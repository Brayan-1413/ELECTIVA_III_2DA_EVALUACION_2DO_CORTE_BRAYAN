# Se importa la librería SQLAlchemy para los tipos de columnas y las relaciones
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Se llama a la dirreccion del archivo donde esta la base de datos
from modelo.base import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, nullable=False)
    
    genero_favorito_id = Column(Integer, ForeignKey('generos.id'), nullable=True)
    
    genero_favorito = relationship('Genero', backref='usuarios_favoritos')

    def __repr__(self):
        return (f"<Usuario(id={self.id}, nombre='{self.nombre}', correo='{self.correo}', "
                f"genero_favorito={self.genero_favorito})>")