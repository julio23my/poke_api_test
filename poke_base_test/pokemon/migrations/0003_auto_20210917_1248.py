# Generated by Django 3.2.7 on 2021-09-17 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_auto_20210917_1246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game_indice',
            options={'verbose_name': 'game_indice', 'verbose_name_plural': 'game_indices'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'type', 'verbose_name_plural': 'types'},
        ),
    ]