from editar.editar_pokemon import editar_pokemon
from editar.editar_entrenador import editar_entrenador

def submenu_editar(tree_pokemons, root_pokemons, pokemons, tree_entrenadores, root_entrenadores, entrenadores):
    while True:
        print("\n--- Submenú de Edición ---")
        print("1. Editar Pokémons")
        print("2. Editar Entrenadores")
        print("3. Regresar al menú principal")

        opcion_editar = int(input("Seleccione una opción: "))

        if opcion_editar == 1:
            editar_pokemon(tree_pokemons, root_pokemons, pokemons)
        elif opcion_editar == 2:
            editar_entrenador(tree_entrenadores, root_entrenadores, entrenadores)
        elif opcion_editar == 3:
            break
        else:
            print("Opción inválida. Intente nuevamente.")