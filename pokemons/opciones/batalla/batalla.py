from pokemons.opciones.batalla.calcular_daño import calcular_daño

def iniciar_batalla(pokemons):
    # Interacción simple para mostrar el daño y reducción de vida de dos pokémones
    pokemon1_id = int(input("Ingrese el ID del primer pokémon: "))
    pokemon2_id = int(input("Ingrese el ID del segundo pokémon: "))

    # Buscar los pokémones seleccionados
    pokemon1 = next((p for p in pokemons if int(p.find('id').text) == pokemon1_id), None)
    pokemon2 = next((p for p in pokemons if int(p.find('id').text) == pokemon2_id), None)

    if pokemon1 and pokemon2:
        daño, ps_afectado = calcular_daño(pokemon1, pokemon2)
        print(f"El daño aplicado a uno de los pokémones ha sido de {daño}.")
        if ps_afectado == int(pokemon2.find('ps').text):
            print(f"PS de {pokemon1.find('nombre').text} después: {pokemon1.find('ps').text}")
            print(f"PS de {pokemon2.find('nombre').text} antes: {ps_afectado}, después: {pokemon2.find('ps').text}")
        else:
            print(f"PS de {pokemon1.find('nombre').text} antes: {ps_afectado}, después: {pokemon1.find('ps').text}")
            print(f"PS de {pokemon2.find('nombre').text} después: {pokemon2.find('ps').text}")
    else:
        print("No se encontraron los pokémones con los ID ingresados.")