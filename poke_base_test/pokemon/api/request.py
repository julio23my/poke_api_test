from os import error
import requests


URL_BASE_POKEMON = 'https://pokeapi.co/api/v2/'


def pokemon_info(self,id):
    dic_pokemon = dict()
    try:
        r = requests.get(URL_BASE_POKEMON+f'pokemon/{id}')
        if r.ok:
            request_information = r.json()
            dic_pokemon['id'] = request_information['id']
            dic_pokemon['name'] = request_information['name'].capitalize()
            dic_pokemon['height'] =request_information['height']
            dic_pokemon['weight'] = request_information['weight']
            dic_pokemon['stats'] = stats(request_information['stats'])
            dic_pokemon['evolution_chain'] = evolution_chain(id)
            if not type(dic_pokemon['evolution_chain']) == list:
                return dic_pokemon['evolution_chain']
                
            return dic_pokemon
        else:
            return f"code {r.reason}, {r.status_code}" 
    except error:

        return "Fetch api pokemon information"



def evolution_chain(id):
    try:
        r = requests.get(URL_BASE_POKEMON+'pokemon')
        r = requests.get(URL_BASE_POKEMON+f'pokemon-species/{id}')
        ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
        list_ordinal = [ordinal(n) for n in range(1,32)]
        list_pokemon = []
        if r.ok:
            dic_json = r.json()
            dic_response = dict()
            dic_evolution = dict(requests.get(dic_json['evolution_chain']['url']).json())
            dic_response[list_ordinal[0]] = dic_evolution['chain']['species']['name'].capitalize()
            list_pokemon.append(dic_response)
            for evolution in dic_evolution['chain']['evolves_to']:
                dic_response=dict()
                if len(dic_evolution['chain']['evolves_to'])>1:
                    dic_response['alternative'] = True
                else:
                    dic_response['alternative'] = False
                dic_response[list_ordinal[1]] = evolution['species']['name'].capitalize()
                list_pokemon.append(dic_response)
                for evolution_2 in evolution['evolves_to']:
                    dic_response = dict()
                    if len(evolution_2['evolves_to'])>1:
                        dic_response['alternative'] = True
                    else:
                        dic_response['alternative'] = False

                    dic_response[list_ordinal[2]] =evolution_2['species']['name'].capitalize()
                    list_pokemon.append(dic_response)
            return list_pokemon
        else:
            return f"code {r.reason}, {r.status_code}"
    except error:
        return "Fetch api evolution"




def stats(stats):
    list_stats = []
    if len(stats) > 0:
        for stat in stats:
            dic_stats = dict()
            dic_stats[stat['stat']['name'].replace("-","_")] = stat['base_stat']
            list_stats.append(dic_stats)

    
    return list_stats
    

