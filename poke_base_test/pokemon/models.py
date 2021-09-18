from django.db import models
from django.urls import reverse

# Create your models here.

class NameTimeStampedModel(models.Model):
    """
    This is the main class of models

    created:    Date create object
    modify:     Date modify
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# POKEMON MOVE
class Move(NameTimeStampedModel):
    
    name = models.CharField('Name', max_length=20, unique=True)

    class Meta:
        verbose_name = ("move")
        verbose_name_plural = ("moves")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("move_detail", kwargs={"pk": self.pk})

# POKEMON ABILITY
class Ability(NameTimeStampedModel):
    
    name = models.CharField('Name', max_length=20, unique=True)


    class Meta:
        verbose_name = ("ability")
        verbose_name_plural = ("abilities")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ability_detail", kwargs={"pk": self.pk})

class Stat(NameTimeStampedModel):
    
    name = models.CharField('Name', max_length=20, unique=True)


    class Meta:
        verbose_name = ("Stat")
        verbose_name_plural = ("Stats")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("stat_detail", kwargs={"pk": self.pk})

# POKEMON FORM
class Form(NameTimeStampedModel):
    name = models.CharField('Name', max_length=20, unique=True)

    

    class Meta:
        verbose_name = ("form")
        verbose_name_plural = ("forms")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("form_detail", kwargs={"pk": self.pk})


# POKEMON FORM
class Type(NameTimeStampedModel):
    name = models.CharField('Name', max_length=20, unique=True)

    

    class Meta:
        verbose_name = ("type")
        verbose_name_plural = ("types")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("type_detail", kwargs={"pk": self.pk})

# POKEMON GAME INDICE
class GameIndice(NameTimeStampedModel):
    
    
    name = models.CharField('Name', max_length=20, unique=True)

    class Meta:
        verbose_name = ("game_indice")
        verbose_name_plural = ("game_indices")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("game_indice_detail", kwargs={"pk": self.pk})




# POKEMON BASE
class Pokemon(NameTimeStampedModel):
    
    id = models.BigAutoField(primary_key=True, unique=True)
    name = models.CharField('Name', max_length=20, unique=True)
    height = models.IntegerField('Height')
    weight = models.IntegerField('Weight')
    evolution = models.ManyToManyField('self', through='PokemonEvolution')
    moves = models.ManyToManyField(Move)
    abilities = models.ManyToManyField(Ability)
    forms = models.ManyToManyField(Form)
    type = models.ManyToManyField(Type)
    game_indices = models.ManyToManyField(GameIndice, through='PokemonGameIndice')
    stat = models.ManyToManyField(Stat, through='PokemonStat')

    class Meta:
        verbose_name = ("pokemon")
        verbose_name_plural = ("pokemons")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pokemon_detail", kwargs={"pk": self.pk})

class PokemonGameIndice(models.Model):
    game_indice = models.ForeignKey(GameIndice, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    game_index = models.IntegerField()

    class Meta:
        verbose_name = ("PokemonGameIndice")
        verbose_name_plural = ("PokemonGameIndices")

    def __str__(self):
        return self.game_indice.name

    def get_absolute_url(self):
        return reverse("pokemon_game_indice_detail", kwargs={"pk": self.pk})


class PokemonStat(models.Model):
    stat = models.ForeignKey(Stat, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    value = models.IntegerField()
    class Meta:
        verbose_name = ("PokemonStat")
        verbose_name_plural = ("PokemonStats")

    def __str__(self):
        return self.stat.name

    def get_absolute_url(self):
        return reverse("stats_detail", kwargs={"pk": self.pk})


class PokemonEvolution(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    evolution = models.ManyToManyField("self")
    pre_evolution = models.ForeignKey("self", on_delete=models.CASCADE, null=True,blank=True)
    is_evolution = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("PokemonEvolution")
        verbose_name_plural = ("PokemonEvolution")

    def __str__(self):
        return self.pokemon.name

    def get_absolute_url(self):
        return reverse("pokemon_evolution_detail", kwargs={"pk": self.pk})