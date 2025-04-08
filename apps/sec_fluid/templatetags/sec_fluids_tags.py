from django import template

register = template.Library()


@register.filter
def properties_data(result):
    """
    Convertit les résultats en une liste de dictionnaires formatés pour l'affichage dans le tableau.
    """
    properties = [
        {
            "key": "temperature",
            "label": "Température",
            "unit": "[°C]",
            "value": result["temperature"],
            "precision": 0,
        },
        {
            "key": "freezing_temperature",
            "label": "Température de congélation",
            "unit": "[°C]",
            "value": result["freezing_temperature"],
            "precision": 2,
        },
        {
            "key": "density",
            "label": "Densité",
            "unit": "[kg/m³]",
            "value": result["density"],
            "precision": 1,
        },
        {
            "key": "specific_heat",
            "label": "Chaleur spécifique",
            "unit": "[J/kg/K]",
            "value": result["specific_heat"],
            "precision": 0,
        },
        {
            "key": "conductivity",
            "label": "Conductivité",
            "unit": "[W/m/K]",
            "value": result["conductivity"],
            "precision": 4,
        },
    ]
    return properties
