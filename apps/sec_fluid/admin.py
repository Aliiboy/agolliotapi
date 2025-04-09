from django.contrib import admin

from .models import IncompressibleMixtureFluid


# Register your models here.
class IncompressibleMixtureFluidAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "temperature_min",
        "temperature_max",
        "temperature_base",
        "concentration_min",
        "concentration_max",
        "created_at",
        "updated_at",
    )
    search_fields = ("name", "description")
    list_filter = ("name", "description")
    ordering = ("name", "description")


admin.site.register(IncompressibleMixtureFluid, IncompressibleMixtureFluidAdmin)
