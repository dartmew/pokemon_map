from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='pokemon_name'
    )
    image = models.ImageField(
        upload_to='pokemon_images',
        blank=True,
        null=True,
        verbose_name='pokemon_image'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='description'
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE,
        related_name='entities',
        verbose_name='pokemon',
        null=True,
        blank=True
    )
    latitude = models.FloatField(
        verbose_name='latitude'
    )
    longitude = models.FloatField(
        verbose_name='longitude'
    )
    appeared_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='appeared_at'
    )
    disappeared_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='disappeared_at'
    )
    level = models.IntegerField(
        default=1,
        verbose_name='Level'
    )
    health = models.IntegerField(
        default=100,
        verbose_name='Health'
    )
    strength = models.IntegerField(
        default=10,
        verbose_name='Strength'
    )
    defense = models.IntegerField(
        default=10,
        verbose_name='Defence'
    )
    stamina = models.IntegerField(
        default=10,
        verbose_name='Stamina'
    )

    def __str__(self):
        return f'{self.pokemon.title}, {self.latitude}, {self.longitude}'