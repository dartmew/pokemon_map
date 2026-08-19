from django.contrib import admin
from .models import Pokemon, PokemonEntity

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'title_en', 'title_jp', 'previous_evolution', 'image')
    fields = ('title', 'title_en', 'title_jp', 'image', 'description', 'previous_evolution')


@admin.register(PokemonEntity)
class PokemonEntityAdmin(admin.ModelAdmin):
    list_display = ('id', 'pokemon', 'latitude', 'longitude', 'appeared_at', 'disappeared_at', 'level', 'health', 'strength', 'defense', 'stamina')
    list_filter = ('pokemon', 'level')
    search_fields = ('pokemon__title',)
    fields = ('pokemon', 'latitude', 'longitude', 'appeared_at', 'disappeared_at', 'level', 'health', 'strength', 'defense', 'stamina')