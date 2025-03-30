from ninja import Field, Query, Router, Schema
from pyfluids import HumidAir, InputHumidAir

from apps.project.api import ErrorResponse

# Création du router pour les endpoints liés à l'air humide
humid_air_router = Router(tags=["Air Humide"])


# Modèle de données pour la requête
class AirPropertyWithTemperatureAndRelativeHumidityRequest(Schema):
    altitude: float = Field(
        default=0,
        ge=-5000,
        le=11000,
        description="Altitude en [m]",
    )
    temperature: float = Field(
        default=20, ge=-143, le=350, description="Température sèche en [°C]"
    )
    relative_humidity: float = Field(
        default=50, ge=0, le=100, description="Humidité relative en [%]"
    )


# Modèle de données pour la réponse
class AirPropertyWithTemperatureAndRelativeHumidityResponse(Schema):
    compressibility: float = Field(
        ..., description="Facteur de compressibilité (sans dimension)"
    )
    conductivity: float = Field(..., description="Conductivité thermique en [W/m/K]")
    density: float = Field(
        ..., description="Densité massique par unité d'air humide en [kg/m³]"
    )
    dew_temperature: float = Field(
        ..., description="Température du point de rosée en [°C]"
    )
    dynamic_viscosity: float = Field(..., description="Viscosité dynamique en [Pa*s]")
    enthalpy: float = Field(
        ..., description="Enthalpie massique spécifique par air humide en [J/kg]"
    )
    entropy: float = Field(
        ..., description="Entropie massique spécifique par air humide en [J/kg/K]"
    )
    humidity: float = Field(..., description="Ratio d'humidité absolue en [kg/kg d.a.]")
    kinematic_viscosity: float = Field(
        ..., description="Viscosité cinématique en [m²/s]"
    )
    partial_pressure: float = Field(
        ..., description="Pression partielle de la vapeur d'eau en [Pa]"
    )
    prandtl: float = Field(..., description="Nombre de Prandtl (sans dimension)")
    pressure: float = Field(..., description="Pression absolue en [Pa]")
    relative_humidity: float = Field(
        ..., description="Ratio d'humidité relative en [%]"
    )
    specific_heat: float = Field(
        ...,
        description="Chaleur spécifique à pression constante par air humide en [J/kg/K]",
    )
    specific_volume: float = Field(
        ..., description="Volume spécifique par unité d'air humide en [m³/kg]"
    )
    temperature: float = Field(..., description="Température sèche en [°C]")
    wet_bulb_temperature: float = Field(..., description="Température humide en [°C]")


@humid_air_router.get(
    "/properties_with_temperature_and_relative_humidity",
    response={
        200: AirPropertyWithTemperatureAndRelativeHumidityResponse,
        400: ErrorResponse,
    },
    summary="Calcule les propriétés de l'air humide.",
)
def calculate_properties_with_temperature_and_relative_humidity(
    request, input: Query[AirPropertyWithTemperatureAndRelativeHumidityRequest]
):
    """
    Calcule les propriétés de l'air humide en fonction de la pression,
    la température sèche et l'humidité relative
    """
    # Création d'un objet d'air humide avec PyFluids
    humid_air = HumidAir().with_state(
        InputHumidAir.altitude(input.altitude),
        InputHumidAir.temperature(input.temperature),
        InputHumidAir.relative_humidity(input.relative_humidity),
    )

    # Récupération de toutes les propriétés demandées
    return humid_air
