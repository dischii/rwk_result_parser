""" RWK IDs for selection of classes in the rwk-shooting website. """
from enum import Enum

class RWKID(Enum):
    """ RWK IDs for selection of classes in the rwk-shooting website. """
    LUFTGEWEHR_2025 = 1905
    LUFTPISTOLE_2025 = 1926
    LUFTGEWEHR_2024 = 1812
    LUFTPISTOLE_2024 = 1813

class CLASSID(Enum):
    """ Class IDs for selection of classes in the rwk-shooting website. """
    OFFENE_KLASSE = "Offene Klasse"
    ALTERSKLASSE = "Altersklasse"
    JUGENDLKLASSE = "Jugendklasse"

class ASSOCIATION(Enum):
    """ Association IDs for selection of classes in the rwk-shooting website. """
    SV_WAPPERSDORF_101052 = "SV Wappersdorf:1"
