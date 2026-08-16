from django.contrib import admin
from .models import Pokemon, PokemonEntity

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')


@admin.register(PokemonEntity)
class PokemonEntityAdmin(admin.ModelAdmin):
    list_display = ('id', 'pokemon', 'latitude', 'longitude')