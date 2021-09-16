from django.core.management.base import BaseCommand, CommandError
import requests

URL_BASE_POKEMON = 'https://pokeapi.co/api/v2/'


class Command(BaseCommand):
    help = 'aaaaaaaa'
    def add_arguments(self, parser):
        parser.add_argument('pokemonid', type=int, help='Id from a pokemon')

    def handle(self, *args, **options):
        r = requests.get(URL_BASE_POKEMON+f'pokemon/{options["pokemonid"]}')
        r2 = requests.get(URL_BASE_POKEMON+f'evolution-chain/{options["pokemonid"]}')
        if r.ok:
            print(r.json()['name'])
            print(r.json()['weight'])
            print(r.json()['height'])
            print("##########STATS##########")
            for stats in r.json()['stats']:
                print(stats['stat']['name']+ ": " + str(stats['base_stat']))
            print(r2.json())
            
        # print()
        # pokemon = pokepy.V2Client().get_pokemon(options['pokemonid'])
        # pokemon = client
        # print(pokemon.id)
        
        # self.stdout.write(self.style.SUCCESS(pokemon.types))
        # self.stdout.write(self.style.SUCCESS(pokemon.weigth))
        # self.stdout.write(self.style.SUCCESS(pokemon.heigth))
        # self.stdout.write(self.style.SUCCESS(pokemon.id))
    