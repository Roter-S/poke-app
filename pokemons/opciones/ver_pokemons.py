def ver_todos_los_pokemons(pokemons):
    for pokemon in pokemons:
        print(f"ID: {pokemon.find('id').text}, Nombre: {pokemon.find('nombre').text}, Tipo: {pokemon.find('tipo').text}, PS: {pokemon.find('ps').text}")

def ver_listado_por_nombre(pokemons):
    pokemons_sorted = sorted(pokemons, key=lambda p: p.find('nombre').text)
    for pokemon in pokemons_sorted:
        print(f"ID: {pokemon.find('id').text}, Nombre: {pokemon.find('nombre').text}, Tipo: {pokemon.find('tipo').text}, PS: {pokemon.find('ps').text}")