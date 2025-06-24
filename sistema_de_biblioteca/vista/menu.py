# Clases importadas de la carpeta 'controlador'
from controlador.genero_controlador import crear_genero, listar_generos
from controlador.libro_controlador import crear_libro, listar_libros, eliminar_libro
from controlador.usuario_controlador import crear_usuario, listar_usuarios, actualizar_usuario

# Menu para realizar operaciones CRUD en la biblioteca
def menu():
    while True:
        print("\n--- Biblioteca CRUD ---")
        print("1. Agregar genero")
        print("2. Ver generos")
        print("3. Agregar libro")
        print("4. Ver libros")
        print("5. Eliminar libro")
        print("6. Agregar usuario")
        print("7. Ver usuarios")
        print("8. Actualizar usuario")
        print("0. Salir")

        opc = input("Elige una opción: ")
        if opc == '1':
            nombre = input("Nombre del genero: ")
            crear_genero(nombre)
        
        elif opc == '2':
            for c in listar_generos():
                print(c)
        
        elif opc == '3':
            titulo = input("Título: ")
            autor = input("Autor: ")
            anio = int(input("Año: "))
            genero_id = int(input("ID del Genero: "))
            crear_libro(titulo, autor, anio, genero_id)
        
        elif opc == '4':
            for l in listar_libros():
                print(l)

        elif opc == '5':
            try:
                id_libro = int(input("ID del libro a eliminar: "))
            except ValueError:
                print("ID inválido.")
                continue

            eliminado = eliminar_libro(id_libro)
            if eliminado:
                print("Libro eliminado correctamente.")

        elif opc == '6':
            nombre = input("Nombre usuario: ")
            correo = input("Correo: ")
            genero_fav = input("ID Genero favorito (opcional): ")
            if genero_fav.strip() == '':
                genero_fav_id = None
            else:
                try:
                    genero_fav_id = int(genero_fav)
                except ValueError:
                    print("ID genero inválido, se asignará None.")
                    genero_fav_id = None
            crear_usuario(nombre, correo, genero_fav_id)
        
        elif opc == '7':
            for u in listar_usuarios():
                print(u)

        elif opc == '8':
            try:
                id_usuario = int(input("ID del usuario a actualizar: "))
            except ValueError:
                print("ID inválido.")
                continue

            nuevo_correo = input("Nuevo correo (deja vacío para no cambiar): ").strip()
            if nuevo_correo == '':
                nuevo_correo = None
            
            genero_fav = input("Nueva ID genero favorito (deja vacío para no cambiar): ").strip()
            if genero_fav == '':
                nuevo_genero_favorito_id = None
            else:
                try:
                    nuevo_genero_favorito_id = int(genero_fav)
                except ValueError:
                    print("ID genero inválido, no se actualizará el genero favorito.")
                    nuevo_genero_favorito_id = None
            
            usuario_actualizado = actualizar_usuario(id_usuario, nuevo_correo, nuevo_genero_favorito_id)
            if usuario_actualizado:
                print(f"Usuario actualizado: {usuario_actualizado}")
            else:
                print("No se pudo actualizar el usuario.")

        elif opc == '0':
            break
        else:
            print("Opción inválida")