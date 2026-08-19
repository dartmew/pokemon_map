from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название покемона (рус.)'
    )
    image = models.ImageField(
        upload_to='pokemon_images',
        blank=True,
        null=True,
        verbose_name='Картинка'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание'
    )
    title_en = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Название на английском'
    )
    title_jp = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Название на японском'
    )
    previous_evolution = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Из кого эволюционировал',
        related_name='next_evolutions'
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE,
        related_name='entities',
        verbose_name='Покемон',
        null=True,
        blank=True
    )
    latitude = models.FloatField(
        verbose_name='Широта'
    )
    longitude = models.FloatField(
        verbose_name='Долгота'
    )
    appeared_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Время появления'
    )
    disappeared_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Время исчезновения'
    )
    level = models.IntegerField(
        default=1,
        verbose_name='Уровень'
    )
    health = models.IntegerField(
        default=100,
        verbose_name='Здоровье'
    )
    strength = models.IntegerField(
        default=10,
        verbose_name='Атака'
    )
    defense = models.IntegerField(
        default=10,
        verbose_name='Защита'
    )
    stamina = models.IntegerField(
        default=10,
        verbose_name='Выносливость'
    )

    def __str__(self):
        return f'{self.pokemon.title}, {self.latitude}, {self.longitude}'