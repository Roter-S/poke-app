import xml.etree.ElementTree as ET

def editar_pokemon(tree_pokemons, root_pokemons, pokemons):
    print("\n--- Editar Pokémons ---")
    print("1. Editar un pokémon existente")
    print("2. Crear un nuevo pokémon")
    print("3. Eliminar un pokémon")
    print("4. Regresar al submenú de edición")

    opcion_editar_pokemon = int(input("Seleccione una opción: "))

    if opcion_editar_pokemon == 1:
        pokemon_id = int(input("Ingrese el ID del pokémon a editar: "))
        pokemon = next((p for p in pokemons if int(p.find('id').text) == pokemon_id), None)
        if pokemon:
            print(f"Editando el pokémon con ID {pokemon_id}")
            nuevo_nombre = input("Nuevo nombre del pokémon: ")
            nuevo_tipo = input("Nuevo tipo del pokémon: ")
            nuevo_ps = input("Nuevo valor de PS del pokémon: ")

            pokemon.find('nombre').text = nuevo_nombre
            pokemon.find('tipo').text = nuevo_tipo
            pokemon.find('ps').text = nuevo_ps

            tree_pokemons.write("pokemons/pokemons.xml")  # Guarda los cambios en el archivo XML
            print("Pokémon editado exitosamente.")
        else:
            print("Pokémon no encontrado.")
    elif opcion_editar_pokemon == 2:
        nuevo_id = len(pokemons) + 1
        nuevo_nombre = input("Nombre del nuevo pokémon: ")
        nuevo_tipo = input("Tipo del nuevo pokémon: ")
        nuevo_ps = input("Valor de PS del nuevo pokémon: ")

        nuevo_pokemon = ET.Element('pokemon')
        ET.SubElement(nuevo_pokemon, 'id').text = str(nuevo_id)
        ET.SubElement(nuevo_pokemon, 'nombre').text = nuevo_nombre
        ET.SubElement(nuevo_pokemon, 'tipo').text = nuevo_tipo
        ET.SubElement(nuevo_pokemon, 'ps').text = nuevo_ps

        root_pokemons.append(nuevo_pokemon)
        tree_pokemons.write("pokemons/pokemons.xml")  # Guarda los cambios en el archivo XML
        print("Pokémon creado exitosamente.")
    elif opcion_editar_pokemon == 3:
        pokemon_id = int(input("Ingrese el ID del pokémon a eliminar: "))
        pokemon = next((p for p in pokemons if int(p.find('id').text) == pokemon_id), None)
        if pokemon:
            root_pokemons.remove(pokemon)
            tree_pokemons.write("pokemons/pokemons.xml")  # Guarda los cambios en el archivo XML
            print("Pokémon eliminado exitosamente.")
        else:
            print("Pokémon no encontrado.")
    elif opcion_editar_pokemon == 4:
        pass  # No hace falta realizar ninguna acción si se elige regresar
    else:
        print("Opción inválida. Intente nuevamente.")