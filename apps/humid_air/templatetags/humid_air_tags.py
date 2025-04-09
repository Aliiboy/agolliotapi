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
            "key": "relative_humidity",
            "label": "Humidité relative",
            "unit": "[%]",
            "value": result["relative_humidity"],
            "precision": 0,
        },
        {
            "key": "wet_bulb_temperature",
            "label": "Température humide",
            "unit": "[°C]",
            "value": result["wet_bulb_temperature"],
            "precision": 2,
        },
        {
            "key": "dew_temperature",
            "label": "Température de rosée",
            "unit": "[°C]",
            "value": result["dew_temperature"],
            "precision": 2,
        },
        # Propriétés intrinsèques
        {
            "key": "partial_pressure",
            "label": "Pression partielle",
            "unit": "[Pa]",
            "value": result["partial_pressure"],
            "precision": 0,
        },
        {
            "key": "humidity",
            "label": "Humidité",
            "unit": "[kg/kg d.a.]",
            "value": result["humidity"],
            "precision": 6,
        },
        {
            "key": "density",
            "label": "Densité",
            "unit": "[kg/m³]",
            "value": result["density"],
            "precision": 4,
        },
        {
            "key": "specific_volume",
            "label": "Volume spécifique",
            "unit": "[m³/kg]",
            "value": result["specific_volume"],
            "precision": 4,
        },
        {
            "key": "enthalpy",
            "label": "Enthalpie",
            "unit": "[J/kg]",
            "value": result["enthalpy"],
            "precision": 0,
        },
        {
            "key": "entropy",
            "label": "Entropie",
            "unit": "[J/kg/K]",
            "value": result["entropy"],
            "precision": 2,
        },
        {
            "key": "specific_heat",
            "label": "Chaleur spécifique",
            "unit": "[J/kg/K]",
            "value": result["specific_heat"],
            "precision": 0,
        },
        {
            "key": "compressibility",
            "label": "Compressibilité",
            "unit": "[-]",
            "value": result["compressibility"],
            "precision": 4,
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
            "unit": "[Pa*s]",
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
