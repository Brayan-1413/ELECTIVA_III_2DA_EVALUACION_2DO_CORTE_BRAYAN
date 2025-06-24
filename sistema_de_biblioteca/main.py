
from modelo.base import Base, engine
from vista.menu import menu
import modelo.genero, modelo.libro, modelo.usuario

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    menu()