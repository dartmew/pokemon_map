import folium
import json
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import Pokemon, PokemonEntity
from django.db import models
from django.utils import timezone


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons_from_db = Pokemon.objects.all()
    pokemons_on_page = []
    for pokemon in pokemons_from_db:
        if pokemon.image:
            img_url = request.build_absolute_uri(pokemon.image.url)
        else:
            img_url = DEFAULT_IMAGE_URL
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': img_url,
            'title_ru': pokemon.title,
        })

    now = timezone.now()
    active_entities = PokemonEntity.objects.filter(
        models.Q(appeared_at__isnull=True) | models.Q(appeared_at__lte=now),
        models.Q(disappeared_at__isnull=True) | models.Q(disappeared_at__gte=now)
    )

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for entity in active_entities:
        pokemon = entity.pokemon
        if pokemon and pokemon.image:
            img_url = request.build_absolute_uri(pokemon.image.url)
        else:
            img_url = DEFAULT_IMAGE_URL
        add_pokemon(folium_map, entity.latitude, entity.longitude, img_url)

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)

    now = timezone.now()
    entities = pokemon.entities.filter(
        models.Q(appeared_at__isnull=True) | models.Q(appeared_at__lte=now),
        models.Q(disappeared_at__isnull=True) | models.Q(disappeared_at__gte=now)
    )

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for entity in entities:
        img_url = request.build_absolute_uri(pokemon.image.url) if pokemon.image else DEFAULT_IMAGE_URL
        add_pokemon(folium_map, entity.latitude, entity.longitude, img_url)

    pokemon_data = {
        'pokemon_id': pokemon.id,
        'title_ru': pokemon.title,
        'img_url': request.build_absolute_uri(pokemon.image.url) if pokemon.image else DEFAULT_IMAGE_URL,
        'description': pokemon.description or '',
        'title_en': getattr(pokemon, 'title_en', ''),
        'previous_evolution': None,
        'next_evolution': None,
        'entities': [{'lat': e.latitude, 'lon': e.longitude} for e in entities],
    }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),
        'pokemon': pokemon_data,
    })
