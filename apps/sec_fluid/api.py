from enum import Enum

from ninja import Field, Query, Router, Schema
from pyfluids import Fluid, FluidsList, Input

from apps.project.api import ErrorResponse

# Création du router pour les endpoints liés aux fluides secondaires
sec_fluid_router = Router(tags=["Fluides Secondaires"])


class MixtureEnum(Enum):
    # mass-based binary mixtures
    FRE = ("FRE", "Freezium, Potassium Formate")
    IceEA = ("IceEA", "Ice slurry with Ethanol")
    IceNA = ("IceNA", "Ice slurry with NaCl")
    IcePG = ("IcePG", "Ice slurry with Propylene Glycol")
    LiBr = ("LiBr", "Lithium-bromide solution – aq")
    MAM = ("MAM", "Ammonia (NH3) – aqueous solution")
    MAM2 = ("MAM2", "Melinder, Ammonia")
    MCA = ("MCA", "Calcium Chloride (CaCl2) – aq")
    MCA2 = ("MCA2", "Melinder, Calcium Chloride")
    MEA = ("MEA", "Ethyl Alcohol (Ethanol) – aq")
    MEA2 = ("MEA2", "Melinder, Ethanol")
    MEG = ("MEG", "Ethylene Glycol – aq")
    MEG2 = ("MEG2", "Melinder, Ethylene Glycol")
    MGL = ("MGL", "Glycerol – aq")
    MGL2 = ("MGL2", "Melinder, Glycerol")
    MITSW = ("MITSW", "MIT Seawater")
    MKA = ("MKA", "Potassium Acetate (CH₃CO₂K) – aq")
    MKA2 = ("MKA2", "Melinder, Potassium Acetate")
    MKC = ("MKC", "Potassium Carbonate (K₂CO₃) – aq")
    MKC2 = ("MKC2", "Melinder, Potassium Carbonate")
    MKF = ("MKF", "Potassium Formate (CHKO₂) – aq")
    MLI = ("MLI", "Lithium Chloride (LiCl) – aq")
    MMA = ("MMA", "Methyl Alcohol (Methanol) – aq")
    MMA2 = ("MMA2", "Melinder, Methanol")
    MMG = ("MMG", "MgCl₂ – aq")
    MMG2 = ("MMG2", "Melinder, Magnesium Chloride")
    MNA = ("MNA", "Sodium Chloride (NaCl) – aq")
    MNA2 = ("MNA2", "Melinder, Sodium Chloride")
    MPG = ("MPG", "Propylene Glycol – aq")
    MPG2 = ("MPG2", "Melinder, Propylene Glycol")
    VCA = ("VCA", "VDI, Calcium Chloride")
    VKC = ("VKC", "VDI, Potassium Carbonate")
    VMA = ("VMA", "VDI, Methanol")
    VMG = ("VMG", "VDI, Magnesium Chloride")
    VNA = ("VNA", "VDI, Sodium Chloride")
    # volume-based binary mixtures
    AEG = ("AEG", "ASHRAE, Ethylene Glycol")
    AKF = ("AKF", "Antifrogen KF, Potassium Formate")
    AL = ("AL", "Antifrogen L, Propylene Glycol")
    AN = ("AN", "Antifrogen N, Ethylene Glycol")
    APG = ("APG", "ASHRAE, Propylene Glycol")
    GKN = ("GKN", "Glykosol N, Ethylene Glycol")
    PK2 = ("PK2", "Pekasol 2000, K acetate/formate")
    PKL = ("PKL", "Pekasol L, Propylene Glycol")
    ZAC = ("ZAC", "Zitrec AC, Corrosion Inhibitor")
    ZFC = ("ZFC", "Zitrec FC, Propylene Glycol")
    ZLC = ("ZLC", "Zitrec LC, Propylene Glycol")
    ZM = ("ZM", "Zitrec M, Ethylene Glycol")
    ZMC = ("ZMC", "Zitrec MC, Ethylene Glycol")

    def __init__(self, code: str, description: str):
        # La valeur officielle de l'enum reste le code
        self._value_ = code
        # On ajoute un attribut pour la description
        self.description = description

    @property
    def value(self):
        return self._value_


# Modèle de données pour la requête
class SecondaryFluidPropertyRequest(Schema):
    mixture_name: MixtureEnum = Field(
        description="Type de fluide secondaire : "
        + "; ".join(f"{m.name}: {m.description}" for m in MixtureEnum),
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
    mixture = input.mixture_name

    # Correction: Utilisation de mixture.value pour obtenir le code de l'enum
    get_fluid_attr = getattr(FluidsList, mixture.value)

    # Création d'un objet fluide avec PyFluids
    sec_fluid = Fluid(get_fluid_attr, input.concentration).with_state(
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
