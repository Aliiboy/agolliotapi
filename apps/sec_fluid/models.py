# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class IncompressibleMixtureFluid(models.Model):
    """
    Modèle pour représenter un fluide à mélange incompressible.
    """

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    temperature_min = models.FloatField()
    temperature_max = models.FloatField()
    temperature_base = models.FloatField()
    concentration_min = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(1)]
    )
    concentration_max = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(1)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " - " + self.description

    class Meta:
        verbose_name = "Fluide à mélange"
        verbose_name_plural = "Fluides à mélange"
