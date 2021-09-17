from django.core.management.base import BaseCommand, CommandError
from poke_base_test.pokemon.api.request import pokemon_info
from django.http import JsonResponse
import json


class Command(BaseCommand):
    help = 'This command gives you information about a pokemon.'
    def add_arguments(self, parser):
        parser.add_argument('pokemonid', type=int, help='Id from a pokemon')

    def handle(self, *args, **options):
        
        pokemon = pokemon_info(self,options['pokemonid'])
        print(pokemon)
        # self.stderr.write(self.style.SUCCESS(pokemon))
        
        
        
        # return date_handler(self,pokemon)
        # print()
        # pokemon = pokepy.V2Client().get_pokemon(options['pokemonid'])
        # pokemon = client
        # print(pokemon.id)
        
        # self.stdout.write(self.style.SUCCESS(pokemon.types))
        # self.stdout.write(self.style.SUCCESS(pokemon.weigth))
        # self.stdout.write(self.style.SUCCESS(pokemon.heigth))
        # self.stdout.write(self.style.SUCCESS(pokemon.id))