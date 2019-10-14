from typing import List

import math

from cta.data.resource_data import ResourceData

from cta.data.resource_configuration_data import ResourceConfigurationData


class ResourceConfigurationsManager:

    def __init__(self, resources: List[ResourceData], single_element_length: List[float]) -> None:
        self._validate_data(resources, single_element_length)
        self._configurations: List[ResourceConfigurationData] = []
        self._single_element_length: List[float] = single_element_length
        self._resources: List[ResourceData] = ResourceConfigurationsManager._sorted_resources(resources)
        self._configuration_starts_at: List[int] = []
        self._init()

    # TODO: raise error while not len(resources)
    # TODO: raise error while there is resources with same length
    @staticmethod
    def _validate_data(resources, single_elements_length) -> None:
        for r in resources:
            for l in single_elements_length:
                if r.length > l:
                    raise ValueError('Single element must be longer than resource!')

    @staticmethod
    def _sorted_resources(resources: List[ResourceData]) -> List[ResourceData]:
        return sorted(resources, key=lambda r: r.length, reverse=True)

    @staticmethod
    def _has_more_configs(x: List[int]) -> bool:
        copy_x = x[:]
        last = copy_x.pop()
        if last == 0:
            return True

        x_sum = 0

        for val in copy_x:
            x_sum += val
            if x_sum:
                return True

        return False

    @staticmethod
    def _can_decrease_on_right(x: List[int], index) -> bool:
        copy_x = x[index + 1: len(x) - 1]
        x_sum = 0

        for val in copy_x:
            x_sum += val
            if x_sum:
                return True

        return False

    @property
    def get_configurations(self) -> List[ResourceConfigurationData]:
        return self._configurations

    @property
    def get_configurations_starts_at(self) -> List[int]:
        return self._configuration_starts_at

    # TODO: to refactor.. seriously..
    # TODO: please approve with this shit
    def _init(self) -> None:
        for i, max_length in enumerate(self._single_element_length):
            self._init_single_configuration(max_length, i == 0)
            self._configuration_starts_at.append(len(self._configurations))

        self._configuration_starts_at.pop()

    def _add_configuration(self, sections: List[int]) -> None:
        for i, configuration in enumerate(self._configurations):
            configuration.sections.append(sections[i])

    def _init_single_configuration(self, single_max_length: float, create: bool) -> None:
        current_config = []

        max_length = single_max_length
        for r in self._resources:
            sections = math.floor(max_length / r.length)
            current_config.append(sections)
            max_length -= sections * r.length
            if create:
                self._configurations.append(
                    ResourceConfigurationData(r, [sections])
                )

        if not create:
            self._add_configuration(current_config)

            # TODO: len(current_config) -> -2
        current_list_index = len(current_config) - 2
        while ResourceConfigurationsManager._has_more_configs(current_config):
            if not current_config[current_list_index]:
                current_list_index -= 1
                continue
            current_config[current_list_index] -= 1

            max_length = single_max_length
            for i in range(current_list_index + 1):
                max_length -= current_config[i] * self._configurations[i].resource.length

            # recalculate all on ->
            for i, sections in enumerate(current_config):
                if i <= current_list_index:
                    continue

                resource_length = self._configurations[i].resource.length
                sections = math.floor(max_length / resource_length)
                current_config[i] = sections
                max_length -= resource_length * sections

            self._add_configuration(current_config)

            while ResourceConfigurationsManager._can_decrease_on_right(current_config, current_list_index):
                tmp_index = len(current_config) - 2
                while not current_config[tmp_index]:
                    tmp_index -= 1

                current_config[tmp_index] -= 1

                max_length = single_max_length
                for i in range(tmp_index + 1):
                    max_length -= current_config[i] * self._configurations[i].resource.length

                # recalculate all on ->
                for i, sections in enumerate(current_config):
                    if i <= tmp_index:
                        continue

                    resource_length = self._configurations[i].resource.length
                    sections = math.floor(max_length / resource_length)
                    current_config[i] = sections
                    max_length -= resource_length * sections

                self._add_configuration(current_config)
