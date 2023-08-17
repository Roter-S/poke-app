# Función para calcular el daño y reducción de vida de dos pokémones
def calcular_daño(pokemon1, pokemon2):
    ataque_pokemon1 = int(pokemon1.find('ataque').text)
    ataque_pokemon2 = int(pokemon2.find('ataque').text)

    if ataque_pokemon1 >= ataque_pokemon2:
        daño = ataque_pokemon1 - ataque_pokemon2
        pokemon2_ps_element = pokemon2.find('ps')
        pokemon2_ps_actual = int(pokemon2_ps_element.text)
        pokemon2_ps_element.text = str(pokemon2_ps_actual - daño)
        return daño, pokemon2_ps_actual
    else:
        daño = ataque_pokemon2 - ataque_pokemon1
        pokemon1_ps_element = pokemon1.find('ps')
        pokemon1_ps_actual = int(pokemon1_ps_element.text)
        pokemon1_ps_element.text = str(pokemon1_ps_actual - daño)
        return daño, pokemon1_ps_actual