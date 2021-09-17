import requests


URL_BASE_POKEMON = 'https://pokeapi.co/api/v2/'


def pokemon_info(self,id):
    dic_pokemon = dict()
    r = requests.get(URL_BASE_POKEMON+f'pokemon/{id}')
    if r.ok:
        self.stdout.write(self.style.WARNING("Information"))
        request_information = r.json()
        dic_pokemon['id'] = request_information['id']
        dic_pokemon['name'] = request_information['name'].capitalize()
        dic_pokemon['height'] =request_information['height']
        dic_pokemon['weight'] = request_information['weight']
        for key in dic_pokemon:
             self.stdout.write(self.style.SUCCESS(key) +": " + str(dic_pokemon[key]) )
        dic_pokemon['stats'] = stats(self,request_information['stats'])
        
        dic_pokemon['evolution_chain'] = evolution_chain(self,id)
        return dic_pokemon


def evolution_chain(self,id):
    r = requests.get(URL_BASE_POKEMON+f'pokemon-species/{id}')
    if r.ok:
        dic_json = r.json()
        dic_response = dict()
        dic_evolution = dict(requests.get(dic_json['evolution_chain']['url']).json())
        self.stdout.write(self.style.WARNING("Evolution Chain"))
        self.stdout.write(self.style.SUCCESS("1st "+dic_evolution['chain']['species']['name'].capitalize()))
        
        if len(dic_evolution['chain']['evolves_to'])>0:
            if len(dic_evolution['chain']['evolves_to'])>1:
                self.stdout.write(self.style.WARNING("Alters"))
            for evolution in dic_evolution['chain']['evolves_to']:
                self.stdout.write(self.style.SUCCESS("2nd "+evolution['species']['name'].capitalize()))
                if len(evolution['evolves_to'])>1:
                    self.stdout.write(self.style.WARNING("Alters"))
                for evolution_2 in evolution['evolves_to']:
                    self.stdout.write(self.style.SUCCESS("3rd "+evolution_2['species']['name'].capitalize()))
        return dic_response        
                



            
        

        
        return dic_json


def stats(self,stats):
    list_stats = []
    if len(stats) > 0:
        self.stdout.write(self.style.WARNING("STATS"))
        for stat in stats:
            dic_stats = dict()
            dic_stats['name'] = stat['stat']['name']
            dic_stats['stats'] = stat['base_stat']
            self.stdout.write(self.style.SUCCESS(dic_stats['name']) +": "+str(dic_stats['stats']))
            list_stats.append(dic_stats)

    
    return list_stats
    

