from django import forms
from django.views.generic import FormView
from pyfluids import HumidAir, InputHumidAir


class HumidAirPropertiesWithTemperatureAndRelativeHumidityForm(forms.Form):
    """Formulaire pour calculer les propriétés de l'air humide avec température et humidité relative"""

    altitude = forms.FloatField(
        initial=0,
        label="Altitude [m]",
        min_value=-5000,
        max_value=11000,
        widget=forms.NumberInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
            }
        ),
    )
    temperature = forms.FloatField(
        initial=20,
        label="Température sèche [°C]",
        min_value=-143,
        max_value=350,
        widget=forms.NumberInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
            }
        ),
    )
    relative_humidity = forms.FloatField(
        initial=50,
        label="Humidité relative [%]",
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
            }
        ),
    )


class HumidAirPropertiesWithTemperatureAndRelativeHumidityView(FormView):
    """Vue pour calculer et afficher les propriétés de l'air humide avec température et humidité relative"""

    template_name = "pages/properties_tdr_hr/index.html"
    form_class = HumidAirPropertiesWithTemperatureAndRelativeHumidityForm

    def form_valid(self, form):
        """Traite le formulaire lorsqu'il est valide"""
        altitude = form.cleaned_data["altitude"]
        temperature = form.cleaned_data["temperature"]
        relative_humidity = form.cleaned_data["relative_humidity"]

        humid_air = HumidAir().with_state(
            InputHumidAir.altitude(altitude),
            InputHumidAir.temperature(temperature),
            InputHumidAir.relative_humidity(relative_humidity),
        )

        result = {
            "compressibility": humid_air.compressibility,
            "conductivity": humid_air.conductivity,
            "density": humid_air.density,
            "dew_temperature": humid_air.dew_temperature,
            "dynamic_viscosity": humid_air.dynamic_viscosity,
            "enthalpy": humid_air.enthalpy,
            "entropy": humid_air.entropy,
            "humidity": humid_air.humidity,
            "kinematic_viscosity": humid_air.kinematic_viscosity,
            "partial_pressure": humid_air.partial_pressure,
            "prandtl": humid_air.prandtl,
            "pressure": humid_air.pressure,
            "relative_humidity": humid_air.relative_humidity,
            "specific_heat": humid_air.specific_heat,
            "specific_volume": humid_air.specific_volume,
            "temperature": humid_air.temperature,
            "wet_bulb_temperature": humid_air.wet_bulb_temperature,
        }

        context = self.get_context_data(form=form)
        context["result"] = result

        return self.render_to_response(context)
