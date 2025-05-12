# Create your views here.


from django.views.generic import FormView
from pyfluids import Fluid, FluidsList, Input

from apps.sec_fluid.forms import (
    IncompressibleMixturePropertiesWithTemperatureAndConcentrationForm,
)


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
