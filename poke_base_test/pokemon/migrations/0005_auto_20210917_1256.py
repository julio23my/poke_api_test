# Generated by Django 3.2.7 on 2021-09-17 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0004_alter_pokemon_evolution'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='game_indice',
            new_name='GameIndice',
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='evolution',
            field=models.ManyToManyField(blank=True, related_name='_pokemon_pokemon_evolution_+', to='pokemon.Pokemon'),
        ),
    ]
