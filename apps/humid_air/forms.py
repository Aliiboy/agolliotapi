from django import forms


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
