from django.db import models
from django.urls import reverse

# Create your models here.

class NameTimeStampedModel(models.Model):
        created = models.DateTimeField(auto_now_add=True)
        modified = models.DateTimeField(auto_now=True)
        name = models.CharField('Name', max_length=20)
        class Meta:
            abstract = True

# POKEMON MOVE
class Move(NameTimeStampedModel):
    
    
    class Meta:
        verbose_name = ("move")
        verbose_name_plural = ("moves")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("move_detail", kwargs={"pk": self.pk})

# POKEMON ABILITY
class Ability(NameTimeStampedModel):
    
    

    class Meta:
        verbose_name = ("ability")
        verbose_name_plural = ("abilities")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ability_detail", kwargs={"pk": self.pk})

# POKEMON FORM
class Form(NameTimeStampedModel):
    
    

    class Meta:
        verbose_name = ("form")
        verbose_name_plural = ("forms")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("form_detail", kwargs={"pk": self.pk})


# POKEMON FORM
class Type(NameTimeStampedModel):
    
    

    class Meta:
        verbose_name = ("type")
        verbose_name_plural = ("types")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("type_detail", kwargs={"pk": self.pk})

# POKEMON GAME INDICE
class GameIndice(NameTimeStampedModel):
    
    
    
    index = models.IntegerField()

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
    height = models.DecimalField('Height', max_digits=5, decimal_places=2)
    Weight = models.DecimalField('Weight', max_digits=5, decimal_places=2)
    evolution = models.ManyToManyField('self',blank=True)
    moves = models.ManyToManyField(Move)
    abilities = models.ManyToManyField(Ability)
    forms = models.ManyToManyField(Form)
    type = models.ManyToManyField(Type)
    game_indices = models.ManyToManyField(GameIndice)

    class Meta:
        verbose_name = ("pokemon")
        verbose_name_plural = ("pokemons")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pokemon_detail", kwargs={"pk": self.pk})

