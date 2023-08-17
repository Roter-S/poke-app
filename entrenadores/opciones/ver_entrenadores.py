def ver_todos_los_entrenadores(entrenadores):
    for entrenador in entrenadores:
        print(f"ID: {entrenador.find('id').text}, Nombre: {entrenador.find('nombre').text}, Edad: {entrenador.find('edad').text}, Cantidad de pokemons: {entrenador.find('cantidadPokemons').text}, Victorias: {entrenador.find('victorias').text}, Derrotas: {entrenador.find('derrotas').text}, Genero: {entrenador.find('genero').text}")

def ver_listado_por_nombre_entrenador(entrenadores):
    entrenadores_sorted = sorted(entrenadores, key=lambda p: p.find('nombre').text)
    for entrenador in entrenadores_sorted:
        print(f"ID: {entrenador.find('id').text}, Nombre: {entrenador.find('nombre').text}, Edad: {entrenador.find('edad').text}, Cantidad de pokemons: {entrenador.find('cantidadPokemons').text}, Victorias: {entrenador.find('victorias').text}, Derrotas: {entrenador.find('derrotas').text}, Genero: {entrenador.find('genero').text}")