from os import error, stat
from poke_base_test.pokemon.models import Ability, Form, GameIndice, Move, Pokemon, PokemonStat, Stat, PokemonGameIndice, PokemonEvolution, Type
import requests

URL_BASE_POKEMON = 'https://pokeapi.co/api/v2/'

def get_all_data():
    r = requests.get(URL_BASE_POKEMON+f'evolution-chain')
    max_count = int(r.json()['count'])
    if r.ok:
        for evolution_chain in range(1,max_count):
            try:
                print(evolution_chain)
                a = requests.get(URL_BASE_POKEMON+f'evolution-chain/{evolution_chain}')
                dic_chain={}
                dic_chain['first'] = []
                dic_chain['second'] = []
                dic_chain['third'] = []
                if a.ok:
                    first_evolution = a.json()['chain']
                    first = first_evolution['species']['name']
                    dic_chain['first'].append({"name": first})
                    if first_evolution['evolves_to'] and len(first_evolution['evolves_to'])>0:
                        for second_evolution in first_evolution['evolves_to']:
                            second = second_evolution['species']['name']
                            dic_chain['second'].append({"name": second})
                            if second_evolution['evolves_to'] and len(second_evolution['evolves_to'])>0:
                                for third_evolution in second_evolution['evolves_to']:
                                    third = third_evolution['species']['name']
                                    dic_chain['third'].append({"name": third})
                            else:
                                pass
                    else:
                        pass
                    a = consult_by_chain(dic_chain)
                    set_evolutions = set_evolution(a)
                else:
                    pass
            except error:
                pass
    
def consult_by_chain(dic_chain):
    for key in dic_chain.keys():
        if dic_chain[key] and len(dic_chain[key]) > 0:
            for pokemon in dic_chain[key]:
                lista_paralelo = []
                name_pokemon = pokemon['name']
                print(name_pokemon)
                r = requests.get(URL_BASE_POKEMON+f"pokemon/{name_pokemon}")
                if r.ok:
                    dic_pokemon = r.json()
                    obj, pokemonobj = Pokemon.objects.get_or_create(
                                            id=dic_pokemon['id'], 
                                            name=dic_pokemon['species']['name'], 
                                            height=int(dic_pokemon['height']),
                                            weight=int(dic_pokemon['weight']),

                                            )
                    pokemon['id'] = dic_pokemon['id']
                    if dic_pokemon['abilities'] and type(dic_pokemon['abilities']) == list:
                        for ability in dic_pokemon['abilities']:
                            objab,created = Ability.objects.get_or_create(name=ability['ability']['name'])
                            obj.abilities.add(objab)
                    else:
                        pass
                    if dic_pokemon['forms'] and type(dic_pokemon['forms']) == list:
                        for forms in dic_pokemon['forms']:
                            objforms,created = Form.objects.get_or_create(name=forms['name'])
                            obj.forms.add(objforms)
                    else:
                        pass
                    if dic_pokemon['game_indices'] and type(dic_pokemon['game_indices']) == list:
                        for game_indices in dic_pokemon['game_indices']:
                            objgame,created = GameIndice.objects.get_or_create(name=game_indices['version']['name'])
                            objggame,created = PokemonGameIndice.objects.get_or_create(pokemon=obj,game_indice=objgame,game_index=game_indices['game_index'])
                            
                    else:
                        pass
                    if dic_pokemon['moves'] and type(dic_pokemon['moves']) == list:
                        for moves in dic_pokemon['moves']:
                            objmoves,created = Move.objects.get_or_create(name=moves['move']['name'])
                            obj.moves.add(objmoves)
                    else:
                        pass
                    if dic_pokemon['stats'] and type(dic_pokemon['stats']) == list:
                        for stats in dic_pokemon['stats']:
                            objstats,created = Stat.objects.get_or_create(name=stats['stat']['name'])
                            objpokemon1, creado = PokemonStat.objects.get_or_create(stat=objstats,pokemon=obj, value=stats['base_stat'])
                    if dic_pokemon['types'] and type(dic_pokemon['types']) == list:
                        for types in dic_pokemon['types']:
                            objmoves,created = Type.objects.get_or_create(name=types['type']['name'])
                            obj.type.add(objmoves)
                    else:
                        pass
                    obj.save()
                    pokemon['obj'] = obj
                    
                    
                else:
                    pass
        else:
            pass
    return dic_chain
            

def set_evolution(dic_chain):
    if 'obj' in dic_chain['first']:
        obj,a = PokemonEvolution.objects.get_or_create(pokemon=dic_chain['first'][0]['obj'], is_evolution=False)
        for second in dic_chain['second']:
            obj2,b = PokemonEvolution.objects.get_or_create(pokemon=second['obj'], is_evolution=True, pre_evolution=obj)
            obj.evolution.add(obj2)

            for third in dic_chain['third']:
                obj3,c =PokemonEvolution.objects.get_or_create(pokemon=third['obj'], is_evolution=True, pre_evolution=obj2)
                obj2.evolution.add(obj3)
        
            



            