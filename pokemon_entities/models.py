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

    def _str_(self):
        return self.title


class PokemonEntity(models.Model):
    latitude = models.FloatField(
        verbose_name='latitude'
    )
    longetude = models.FloatField(
        verbose_name='longetude'
    )

    def _str_(self):
        return self.latitude, self.longetude