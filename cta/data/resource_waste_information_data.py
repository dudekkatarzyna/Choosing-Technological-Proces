from dataclasses import dataclass
from typing import List


@dataclass
class ResourcesWasteInformationData:
    waste: List[float]
    price: List[float]
