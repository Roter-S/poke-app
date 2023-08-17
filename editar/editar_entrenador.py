import xml.etree.ElementTree as ET

def editar_entrenador(tree_entrenadores, root_entrenadores, entrenadores):
    print("\n--- Editar Entrenadores ---")
    print("1. Editar un entrenador existente")
    print("2. Crear un nuevo entrenador")
    print("3. Eliminar un entrenador")
    print("4. Regresar al submenú de edición")

    opcion_editar_entrenador = int(input("Seleccione una opción: "))

    if opcion_editar_entrenador == 1:
        entrenador_id = int(input("Ingrese el ID del entrenador a editar: "))
        entrenador = next((e for e in entrenadores if int(e.find('id').text) == entrenador_id), None)
        if entrenador:
            print(f"Editando al entrenador con ID {entrenador_id}")
            nuevo_nombre = input("Nuevo nombre del entrenador: ")
            nueva_edad = input("Nueva edad del entrenador: ")
            nueva_cantidad_pokemons = input("Nueva cantidad de Pokémons del entrenador: ")
            nuevas_victorias = input("Nuevas victorias del entrenador: ")
            nuevas_derrotas = input("Nuevas derrotas del entrenador: ")
            nuevo_genero = input("Nuevo género del entrenador: ")

            entrenador.find('nombre').text = nuevo_nombre
            entrenador.find('edad').text = nueva_edad
            entrenador.find('cantidadPokemons').text = nueva_cantidad_pokemons
            entrenador.find('victorias').text = nuevas_victorias
            entrenador.find('derrotas').text = nuevas_derrotas
            entrenador.find('genero').text = nuevo_genero

            tree_entrenadores.write("entrenadores/entrenadores.xml")  # Guarda los cambios en el archivo XML
            print("Entrenador editado exitosamente.")
        else:
            print("Entrenador no encontrado.")
    elif opcion_editar_entrenador == 2:
        nuevo_id = len(entrenadores) + 1
        nuevo_nombre = input("Nombre del nuevo entrenador: ")
        nueva_edad = input("Edad del nuevo entrenador: ")
        nueva_cantidad_pokemons = input("Cantidad de Pokémons del nuevo entrenador: ")
        nuevas_victorias = input("Victorias del nuevo entrenador: ")
        nuevas_derrotas = input("Derrotas del nuevo entrenador: ")
        nuevo_genero = input("Género del nuevo entrenador: ")

        nuevo_entrenador = ET.Element('entrenador')
        ET.SubElement(nuevo_entrenador, 'id').text = str(nuevo_id)
        ET.SubElement(nuevo_entrenador, 'nombre').text = nuevo_nombre
        ET.SubElement(nuevo_entrenador, 'edad').text = nueva_edad
        ET.SubElement(nuevo_entrenador, 'cantidadPokemons').text = nueva_cantidad_pokemons
        ET.SubElement(nuevo_entrenador, 'victorias').text = nuevas_victorias
        ET.SubElement(nuevo_entrenador, 'derrotas').text = nuevas_derrotas
        ET.SubElement(nuevo_entrenador, 'genero').text = nuevo_genero

        root_entrenadores.append(nuevo_entrenador)
        tree_entrenadores.write("entrenadores/entrenadores.xml")  # Guarda los cambios en el archivo XML
        print("Entrenador creado exitosamente.")
    elif opcion_editar_entrenador == 3:
        entrenador_id = int(input("Ingrese el ID del entrenador a eliminar: "))
        entrenador = next((e for e in entrenadores if int(e.find('id').text) == entrenador_id), None)
        if entrenador:
            root_entrenadores.remove(entrenador)
            tree_entrenadores.write("entrenadores/entrenadores.xml")  # Guarda los cambios en el archivo XML
            print("Entrenador eliminado exitosamente.")
        else:
            print("Entrenador no encontrado.")
    elif opcion_editar_entrenador == 4:
        pass  # No hace falta realizar ninguna acción si se elige regresar
    else:
        print("Opción inválida. Intente nuevamente.")