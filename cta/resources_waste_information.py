from typing import List

from cta import ResourceConfigurationData
from cta.data.resource_waste_information_data import ResourcesWasteInformationData


class ResourcesWasteInformation:

    @staticmethod
    def collect_data(resource_configurations: List[ResourceConfigurationData],
                     resource_configurations_starts_at: List[int],
                     single_element_length: List[float], price_per_unit: float) -> ResourcesWasteInformationData:

        waste, price = ResourcesWasteInformation._calculate_waste_and_price(
            resource_configurations,
            resource_configurations_starts_at,
            single_element_length,
            price_per_unit
        )

        return ResourcesWasteInformationData(
            waste=waste,
            price=price,
        )

    @staticmethod
    def _calculate_waste_and_price(
            resource_configurations: List[ResourceConfigurationData],
            resource_configurations_starts_at: List[int],
            single_elements_length: List[float],
            price_per_unit: float
    ) -> (List[float], List[float]):
        waste = []
        price = []

        starts_at = [0] + resource_configurations_starts_at[:]

        for i, start_index in enumerate(starts_at):
            end_index = starts_at[i + 1] if i < len(starts_at) - 1 else len(resource_configurations[0].sections)

            for j in range(start_index, end_index):
                waste_tmp = single_elements_length[i]
                for conf in resource_configurations:
                    waste_tmp -= conf.sections[j] * conf.resource.length

                waste_tmp = round(waste_tmp, 2)
                waste.append(waste_tmp)
                price.append(waste_tmp * price_per_unit)

        return waste, price
