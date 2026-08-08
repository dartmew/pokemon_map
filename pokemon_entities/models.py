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