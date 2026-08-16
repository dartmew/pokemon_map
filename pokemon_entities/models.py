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

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE,
        related_name='entites',
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

    def __str__(self):
        return f'{self.pokemon.title}, {self.latitude}, {self.longitude}'