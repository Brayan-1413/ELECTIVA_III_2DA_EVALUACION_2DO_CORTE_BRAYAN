# Se importa la librería SQLAlchemy para los tipos de columnas 
from sqlalchemy import Column, Integer, String

# Se llama a la dirreccion del archivo donde esta la base de datos
from modelo.base import Base

# Clase que define el modelo de la tabla 'genero' con SQLAlchemy
class Genero(Base):
    __tablename__ = 'generos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

    def __repr__(self):
        return f"<Genero(id={self.id}, nombre='{self.nombre}')>"