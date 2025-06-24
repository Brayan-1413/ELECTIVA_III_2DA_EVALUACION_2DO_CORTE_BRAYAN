'''Se importa la libreria SQLAlchemy para definir modelos, 
    crear el motor de base de datos y manejar sesiones'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///biblioteca.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)