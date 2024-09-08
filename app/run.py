from service.pokemon import get_primary_infos, get_level, get_pokemon_by_level, get_pokemon_gif
from type.pokemon_service import PokemonDTO

pokemon_name: str = "rattata"
pokemon: PokemonDTO = {"current_level_xp": 1050}

results, validation = get_primary_infos(pokemon_name)
if not validation:
    exit(1)

pokemon['level'], pokemon["initial_level_xp"], pokemon["finally_level_xp"] = get_level(results["growth_url"], pokemon["current_level_xp"])
pokemon["name"] = get_pokemon_by_level(results["evolution_url"], pokemon['level'])
pokemon["gif"] = get_pokemon_gif(pokemon["name"])

print(pokemon)
