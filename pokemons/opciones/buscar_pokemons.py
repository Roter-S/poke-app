import xml.etree.ElementTree as ET

def buscar_por_id(pokemons):
    pokemon_id = int(input("Ingrese el ID del pokémon a buscar: "))
    pokemon = next((p for p in pokemons if int(p.find('id').text) == pokemon_id), None)
    if pokemon:
        print(f"ID: {pokemon.find('id').text}, Nombre: {pokemon.find('nombre').text}, Tipo: {pokemon.find('tipo').text}, PS: {pokemon.find('ps').text}")
    else:
        print("Pokémon no encontrado.")

def buscar_por_nombre(pokemons):
    pokemon_nombre = input("Ingrese el nombre del pokémon a buscar: ")
    pokemon = next((p for p in pokemons if p.find('nombre').text.lower() == pokemon_nombre.lower()), None)
    if pokemon:
        print(f"ID: {pokemon.find('id').text}, Nombre: {pokemon.find('nombre').text}, Tipo: {pokemon.find('tipo').text}, PS: {pokemon.find('ps').text}")
    else:
        print("Pokémon no encontrado.")