from django import template

register = template.Library()


@register.filter
def properties_data(result):
    """
    Convertit les résultats en une liste de dictionnaires formatés pour l'affichage dans le tableau.
    """
    properties = [
        {
            "key": "pressure",
            "label": "Pression",
            "unit": "[Pa]",
            "value": result["pressure"],
            "precision": 0,
        },
        {
            "key": "temperature",
            "label": "Température",
            "unit": "[°C]",
            "value": result["temperature"],
            "precision": 2,
        },
        {
            "key": "concentration",
            "label": "Concentration",
            "unit": "[%]",
            "value": result["concentration"],
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
            "key": "max_temperature",
            "label": "Température maximale",
            "unit": "[°C]",
            "value": result["max_temperature"],
            "precision": 0,
        },
        {
            "key": "min_temperature",
            "label": "Température minimale",
            "unit": "[°C]",
            "value": result["min_temperature"],
            "precision": 0,
        },
        # Propriétés intrinsèques
        {
            "key": "density",
            "label": "Densité",
            "unit": "[kg/m³]",
            "value": result["density"],
            "precision": 1,
        },
        {
            "key": "specific_volume",
            "label": "Volume spécifique",
            "unit": "[m³/kg]",
            "value": result["specific_volume"],
            "precision": 4,
        },
        {
            "key": "specific_heat",
            "label": "Chaleur spécifique",
            "unit": "[J/kg/K]",
            "value": result["specific_heat"],
            "precision": 0,
        },
        # Propriétés de transport
        {
            "key": "conductivity",
            "label": "Conductivité",
            "unit": "[W/m/K]",
            "value": result["conductivity"],
            "precision": 4,
        },
        {
            "key": "dynamic_viscosity",
            "label": "Viscosité dynamique",
            "unit": "[Pa·s]",
            "value": result["dynamic_viscosity"],
            "precision": 10,
        },
        {
            "key": "kinematic_viscosity",
            "label": "Viscosité cinématique",
            "unit": "[m²/s]",
            "value": result["kinematic_viscosity"],
            "precision": 10,
        },
        {
            "key": "prandtl",
            "label": "Nombre de Prandtl",
            "unit": "[-]",
            "value": result["prandtl"],
            "precision": 4,
        },
    ]
    return properties
