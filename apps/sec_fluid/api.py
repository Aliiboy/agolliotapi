from ninja import Field, Query, Router, Schema
from pyfluids import Fluid, FluidsList, Input

from apps.project.api import ErrorResponse

# Création du router pour les endpoints liés aux fluides secondaires
sec_fluid_router = Router(tags=["Fluides Secondaires"])


# Modèle de données pour la requête
class SecondaryFluidPropertyRequest(Schema):
    mixture_name: str = Field(
        default="AEG",
        description="Type de fluide secondaire (AEG: Ethylene Glycol, APG: Propylene Glycol)",
    )
    temperature: float = Field(
        default=20,
        le=100,
        description="Température en [°C]",
    )
    concentration: float = Field(
        default=30,
        ge=0,
        le=100,
        description="Concentration en [%]",
    )


# Modèle de données pour la réponse
class SecondaryFluidPropertyResponse(Schema):
    temperature: float = Field(
        ...,
        description="Température en [°C]",
    )
    freezing_temperature: float = Field(
        ...,
        description="Température de congélation en [°C]",
    )
    density: float = Field(
        ...,
        description="Densité en [kg/m³]",
    )
    specific_heat: float = Field(
        ...,
        description="Chaleur spécifique en [J/kg/K]",
    )
    conductivity: float = Field(
        ...,
        description="Conductivité thermique en [W/m/K]",
    )


def get_fluid_type(mixture_name: str):
    """Convertit le nom du mélange en objet FluidsList correspondant"""
    fluid_types = {
        "AEG": FluidsList.AEG,
        "APG": FluidsList.APG,
    }
    return fluid_types[mixture_name]


@sec_fluid_router.get(
    "/properties_with_temperature_and_concentration",
    response={200: SecondaryFluidPropertyResponse, 400: ErrorResponse},
    summary="Calcule les propriétés des fluides secondaires",
)
def calculate_properties(request, input: Query[SecondaryFluidPropertyRequest]):
    """
    Calcule les propriétés des fluides secondaires (éthylène glycol ou propylène glycol)
    en fonction de la température et de la concentration
    """
    # Conversion du nom du mélange en type de fluide
    fluid_type = get_fluid_type(input.mixture_name)

    # Création d'un objet fluide avec PyFluids
    sec_fluid = Fluid(fluid_type, input.concentration).with_state(
        Input.pressure(101325),
        Input.temperature(input.temperature),
    )

    # Récupération des propriétés demandées
    return {
        "temperature": sec_fluid.temperature,
        "freezing_temperature": sec_fluid.freezing_temperature,
        "density": sec_fluid.density,
        "specific_heat": sec_fluid.specific_heat,
        "conductivity": sec_fluid.conductivity,
    }
