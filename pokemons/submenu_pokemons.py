from pokemons.opciones.ver_pokemons import ver_todos_los_pokemons, ver_listado_por_nombre
from pokemons.opciones.buscar_pokemons import buscar_por_id, buscar_por_nombre

# Función para mostrar el submenú de opciones relacionadas con Pokémon
def submenu_pokemons(pokemons):
    while True:
        print("\n--- Submenú de Opciones de Pokémon ---")
        print("1. Ver todos los pokémons")
        print("2. Ver listado por nombre")
        print("3. Buscar por ID")
        print("4. Buscar por nombre")
        print("5. Regresar al menu principal")

        opcion_pokemon = int(input("Seleccione una opción: "))

        if opcion_pokemon == 1:
            ver_todos_los_pokemons(pokemons)
        elif opcion_pokemon == 2:
            ver_listado_por_nombre(pokemons)
        elif opcion_pokemon == 3:
            buscar_por_id(pokemons)
        elif opcion_pokemon == 4:
            buscar_por_nombre(pokemons)
        elif opcion_pokemon == 5:
            break
        else:
            print("Opción inválida. Intente nuevamente.")