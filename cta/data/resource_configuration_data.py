from dataclasses import dataclass
from typing import List

from cta.data.resource_data import ResourceData


@dataclass
class ResourceConfigurationData:
    resource: ResourceData
    sections: List[int]
