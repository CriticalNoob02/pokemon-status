from service.pokemon import get_primary_infos, get_level, get_pokemon_by_level
from type.pokemon_service import PokemonDTO

results, validation = get_primary_infos("rattata")

if not validation:
    exit(1)

pokemon: PokemonDTO = {}
pokemon["current_level_xp"] = 1000

pokemon['level'], pokemon["initial_level_xp"], pokemon["finally_level_xp"] = get_level(results["growth_url"], pokemon["current_level_xp"])

pokemon["name"] = get_pokemon_by_level(results["evolution_url"], pokemon['level'])


