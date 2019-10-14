from dataclasses import dataclass
from typing import List

from cta.data.resource_waste_information_data import ResourcesWasteInformationData
from cta.data.resource_configuration_data import ResourceConfigurationData


@dataclass
class ChoosingTechnologicalProcessResultsData:
    fun: float
    x: List[int]
    total_waste: float
    total_price: float
    resources_configurations: List[ResourceConfigurationData]
    resources_configurations_starts_at: List[int]
    resources_waste: ResourcesWasteInformationData
