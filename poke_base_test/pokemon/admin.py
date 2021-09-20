from django.contrib import admin
from .models import Pokemon, Ability, GameIndice, Stat,PokemonStat,PokemonEvolution

class PokemonAdmin(admin.ModelAdmin):
    search_fields = ['name']
    pass
    

admin.site.register(Pokemon, PokemonAdmin)

class AbilityAdmin(admin.ModelAdmin):
    pass
    

admin.site.register(Ability, AbilityAdmin)

class GameIndiceAdmin(admin.ModelAdmin):
    pass
    

admin.site.register(GameIndice, GameIndiceAdmin)

class PokemonStatAdmin(admin.ModelAdmin):
    pass
    

admin.site.register(PokemonStat, PokemonStatAdmin)


class PokemonEvolutionAdmin(admin.ModelAdmin):
    pass
    

admin.site.register(PokemonEvolution, PokemonEvolutionAdmin)