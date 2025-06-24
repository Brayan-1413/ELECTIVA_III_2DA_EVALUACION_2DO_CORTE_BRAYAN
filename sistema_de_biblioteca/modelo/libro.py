# Se importa la librería SQLAlchemy para los tipos de columnas y las relaciones
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Se llama a la dirreccion del archivo donde esta la base de datos
from modelo.base import Base

class Libro(Base):
    __tablename__ = 'libros'

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    anio_publicacion = Column(Integer)
    genero_id = Column(Integer, ForeignKey('generos.id'))

    genero = relationship("Genero")

    def __repr__(self):
        return f"<Libro(id={self.id}, titulo='{self.titulo}', autor='{self.autor}')>"

