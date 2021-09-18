from django.core.management.base import BaseCommand, CommandError
from poke_base_test.pokemon.api.scrapper import get_all_data




class Command(BaseCommand):
    help = 'This command gives you information about a pokemon.'
    # def add_arguments(self, parser):
    #     parser.add_argument('pokemonid', type=int, help='Id from a pokemon')

    def handle(self, *args, **options):
        
        pokemon = get_all_data()

        