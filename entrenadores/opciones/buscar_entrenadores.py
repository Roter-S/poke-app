def buscar_por_id(entrenadores):
    entrenador_id = int(input("Ingrese el ID del pokémon a buscar: "))
    entrenador = next((p for p in entrenadores if int(p.find('id').text) == entrenador_id), None)
    if entrenador:
        print(f"ID: {entrenador.find('id').text}, Nombre: {entrenador.find('nombre').text}, Edad: {entrenador.find('edad').text}, Cantidad de pokemons: {entrenador.find('cantidadPokemons').text}, Victorias: {entrenador.find('victorias').text}, Derrotas: {entrenador.find('derrotas').text}, Genero: {entrenador.find('genero').text}")
    else:
        print("Pokémon no encontrado.")

def buscar_por_nombre(entrenadores):
    entrenador_nombre = input("Ingrese el nombre del entrenador a buscar: ")
    entrenador = next((p for p in entrenadores if p.find('nombre').text.lower() == entrenador_nombre.lower()), None)
    if entrenador:
        print(f"ID: {entrenador.find('id').text}, Nombre: {entrenador.find('nombre').text}, Edad: {entrenador.find('edad').text}, Cantidad de pokemons: {entrenador.find('cantidadPokemons').text}, Victorias: {entrenador.find('victorias').text}, Derrotas: {entrenador.find('derrotas').text}, Genero: {entrenador.find('genero').text}")
    else:
        print("Entrenador no encontrado.")