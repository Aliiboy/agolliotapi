from django.views.generic import FormView
from pyfluids import HumidAir, InputHumidAir

from apps.humid_air.forms import (
    HumidAirPropertiesWithTemperatureAndRelativeHumidityForm,
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
