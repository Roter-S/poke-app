import xml.etree.ElementTree as ET
from pokemons.opciones.batalla.batalla import iniciar_batalla
from pokemons.submenu_pokemons import submenu_pokemons
from entrenadores.submenu_entrenadores import submenu_entrenadores
from editar.submenu_editar import submenu_editar

# Leer el archivo XML y obtener la lista de entrenadores
tree_entrenadores = ET.parse("entrenadores/entrenadores.xml") # Actualiza la ruta del archivo XML de los entrenadores
root_entrenadores = tree_entrenadores.getroot()
entrenadores = root_entrenadores.findall('entrenador')

# Leer el archivo XML y obtener la lista de pokémones
tree_pokemons = ET.parse("pokemons/pokemons.xml") # Actualiza la ruta del archivo XML de los pokemones
root_pokemons = tree_pokemons.getroot()
pokemons = root_pokemons.findall('pokemon')

# Función para mostrar el menú principal
def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar Batalla")
        print("2. Ver Pokémons")
        print("3. Ver Entrenadores")
        print("4. Editar Listado")
        print("5. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            iniciar_batalla(pokemons)
        elif opcion == 2:
            submenu_pokemons(pokemons)
        elif opcion == 3:
            submenu_entrenadores(entrenadores)
        elif opcion == 4:
            submenu_editar(tree_pokemons, root_pokemons, pokemons, tree_entrenadores, root_entrenadores, entrenadores)
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Llamada al menú principal para iniciar la aplicación
menu_principal()