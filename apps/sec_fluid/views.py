# Create your views here.


from django import forms
from django.core.exceptions import ValidationError
from django.views.generic import FormView
from pyfluids import Fluid, FluidsList, Input

from .models import IncompressibleMixtureFluid


class IncompressibleMixturePropertiesWithTemperatureAndConcentrationForm(forms.Form):
    """Formulaire pour calculer les propriétés des fluides secondaires à mélange"""

    mixture_name = forms.ModelChoiceField(
        queryset=IncompressibleMixtureFluid.objects.all(),
        label="Nom du mélange",
        widget=forms.Select(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
            }
        ),
    )

    temperature = forms.FloatField(
        initial=20,
        label="Température (°C)",
        widget=forms.NumberInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
            }
        ),
    )

    concentration = forms.FloatField(
        initial=30,
        label="Concentration (%)",
        widget=forms.NumberInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
            }
        ),
    )

    def clean(self):
        """Validation personnalisée pour les champs temperature et concentration"""
        cleaned_data = super().clean()
        mixture = cleaned_data.get("mixture_name")
        temperature = cleaned_data.get("temperature")
        concentration = cleaned_data.get("concentration")

        if mixture and temperature is not None:
            if temperature < mixture.temperature_min:
                raise ValidationError(
                    f"La température doit être supérieure à {mixture.temperature_min}°C"
                )
            if temperature > mixture.temperature_max:
                raise ValidationError(
                    f"La température doit être inférieure à {mixture.temperature_max}°C"
                )

        if mixture and concentration is not None:
            if concentration < mixture.concentration_min * 100:
                raise ValidationError(
                    f"La concentration doit être supérieure à {mixture.concentration_min * 100}%"
                )
            if concentration > mixture.concentration_max * 100:
                raise ValidationError(
                    f"La concentration doit être inférieure à {mixture.concentration_max * 100}%"
                )

        return cleaned_data


class IncompressibleMixturePropertiesWithTemperatureAndConcentrationView(FormView):
    """Vue pour calculer et afficher les propriétés des fluides secondaires à mélange"""

    template_name = "pages/properties_temp_conc/index.html"
    form_class = IncompressibleMixturePropertiesWithTemperatureAndConcentrationForm

    def form_valid(self, form):
        """Traite le formulaire lorsqu'il est valide"""
        mixture = form.cleaned_data["mixture_name"]
        temperature = form.cleaned_data["temperature"]
        concentration = form.cleaned_data["concentration"]

        get_fluid_attr = getattr(FluidsList, mixture.name)

        sec_fluid = Fluid(get_fluid_attr, concentration).with_state(
            Input.pressure(101325),
            Input.temperature(temperature),
        )

        result = {
            "temperature": sec_fluid.temperature,
            "concentration": sec_fluid.fraction,
            "conductivity": sec_fluid.conductivity,
            "density": sec_fluid.density,
            "dynamic_viscosity": sec_fluid.dynamic_viscosity,
            "freezing_temperature": sec_fluid.freezing_temperature,
            "kinematic_viscosity": sec_fluid.kinematic_viscosity,
            "max_temperature": sec_fluid.max_temperature,
            "min_temperature": sec_fluid.min_temperature,
            "prandtl": sec_fluid.prandtl,
            "pressure": sec_fluid.pressure,
            "specific_heat": sec_fluid.specific_heat,
            "specific_volume": sec_fluid.specific_volume,
        }

        context = self.get_context_data(form=form)
        context["result"] = result

        return self.render_to_response(context)
