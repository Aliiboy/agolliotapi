# Create your views here.


from django import forms
from django.views.generic import FormView
from pyfluids import Fluid, FluidsList, Input


def get_fluid_type(mixture_name: str):
    """Convertit le nom du mélange en objet FluidsList correspondant"""
    fluid_types = {
        "AEG": FluidsList.AEG,
        "APG": FluidsList.APG,
    }
    return fluid_types[mixture_name]


class IncompressibleVolumeBasedMixturePropertiesWithTemperatureAndConcentrationForm(
    forms.Form
):
    """Formulaire pour calculer les propriétés des fluides secondaires à mélange"""

    mixture_name = forms.ChoiceField(
        initial="AEG",
        label="Nom du mélange",
        choices=[
            (FluidsList.AEG, "Ethylene Glycol"),
            (FluidsList.APG, "Propylene Glycol"),
        ],
        widget=forms.Select(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
            }
        ),
    )

    temperature = forms.FloatField(
        initial=20,
        label="Température (°C)",
        max_value=100,
        widget=forms.NumberInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
            }
        ),
    )

    concentration = forms.FloatField(
        initial=30,
        label="Concentration (%)",
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
            }
        ),
    )


class IncompressibleVolumeBasedMixturePropertiesWithTemperatureAndConcentrationView(
    FormView
):
    """Vue pour calculer et afficher les propriétés des fluides secondaires à mélange"""

    template_name = "pages/properties_temp_conc/index.html"
    form_class = (
        IncompressibleVolumeBasedMixturePropertiesWithTemperatureAndConcentrationForm
    )

    def form_valid(self, form):
        """Traite le formulaire lorsqu'il est valide"""
        mixture_name = form.cleaned_data["mixture_name"]
        temperature = form.cleaned_data["temperature"]
        concentration = form.cleaned_data["concentration"]

        # Convertir le nom du mélange en objet FluidsList
        fluid_type = get_fluid_type(mixture_name)

        sec_fluid = Fluid(fluid_type, concentration).with_state(
            Input.pressure(101325),
            Input.temperature(temperature),
        )

        result = {
            "temperature": sec_fluid.temperature,
            "freezing_temperature": sec_fluid.freezing_temperature,
            "density": sec_fluid.density,
            "specific_heat": sec_fluid.specific_heat,
            "conductivity": sec_fluid.conductivity,
        }

        context = self.get_context_data(form=form)
        context["result"] = result

        return self.render_to_response(context)
