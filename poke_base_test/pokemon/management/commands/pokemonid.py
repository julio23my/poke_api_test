from django.core.management.base import BaseCommand, CommandError
from poke_base_test.pokemon.api.request import pokemon_info




class Command(BaseCommand):
    help = 'This command gives you information about a pokemon.'
    def add_arguments(self, parser):
        parser.add_argument('pokemonid', type=int, help='Id from a pokemon')

    def handle(self, *args, **options):
        
        pokemon = pokemon_info(self,options['pokemonid'])

        if type(pokemon) == dict:
            self.stdout.write(self.style.WARNING('Information'))
            for poke in pokemon:
                if type(pokemon[poke]) == list and len(pokemon[poke]) > 0:
                    second_level = pokemon[poke]
                    self.stdout.write(self.style.WARNING(poke.capitalize().replace("_"," ")))
                    for i,data in enumerate(second_level):
                        for key2,value in data.items():
                            if key2 == 'alternative':
                                if value ==True:
                                    self.stdout.write(self.style.ERROR(key2.capitalize()))
                                else:
                                    continue
                            else:
                                self.stdout.write(self.style.SUCCESS(key2.capitalize().replace("_"," ")) + ": " +str(value))
                else:
                    self.stdout.write(self.style.SUCCESS(poke.capitalize().replace("_"," "))+": "+ str(pokemon[poke]))
        else:
            self.stdout.write(self.style.ERROR("Error in consulting api: "+ str(pokemon)))
