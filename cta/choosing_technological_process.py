from typing import List

import math
from scipy.optimize import minimize

from cta import ResourceConfigurationData
from cta.data import ChoosingTechnologicalProcessResultsData, ResourceData, ResourcesWasteInformationData
from cta.resource_configurations_manager import ResourceConfigurationsManager
from cta.resources_waste_information import ResourcesWasteInformation


class ChoosingTechnologicalProcess:

    def __init__(self, resources: List[ResourceData], single_elements_length: List[float],
                 price_per_unit: float) -> None:
        self._price_per_unit: float = price_per_unit
        self._single_elements_length: List[float] = single_elements_length
        self._configurations_manager = ResourceConfigurationsManager(resources, single_elements_length)
        self._resources_waste_data: ResourcesWasteInformationData = ResourcesWasteInformation.collect_data(
            self._configurations_manager.get_configurations,
            self._configurations_manager.get_configurations_starts_at,
            self._single_elements_length,
            self._price_per_unit
        )
        # TODO: split to different methods

    def solve(self):
        res = minimize(
            self._f,
            [0] * len(self._configurations_manager.get_configurations[0].sections),
            method='SLSQP',
            bounds=self._bounds(),
            constraints=self._cons(),
        )
        # for change stopping criteria
        # options={'ftol': 1e-100}

        print(res)

        int_x = [self._custom_ceil(x) for x in res.x]

        total_waste = sum([self._resources_waste_data.waste[i] * x for (i, x) in enumerate(int_x)])
        total_price = sum([self._resources_waste_data.price[i] * x for (i, x) in enumerate(int_x)])

        return ChoosingTechnologicalProcessResultsData(
            fun=self._custom_ceil(res.fun),
            x=int_x,
            resources_configurations=self._configurations_manager.get_configurations,
            resources_configurations_starts_at=self._configurations_manager.get_configurations_starts_at,
            resources_waste=self._resources_waste_data,
            total_waste=total_waste,
            total_price=total_price
        )

    def _f(self, x) -> float:
        waste = self._resources_waste_data.waste
        r = 0
        for i, val in enumerate(x):
            r += waste[i] * val

        return r

    @staticmethod
    def _generic_con(x, conf_data: ResourceConfigurationData):
        mat = conf_data.sections
        offset = conf_data.resource.amount
        c = 0
        for i, val in enumerate(x):
            c += mat[i] * val

        return c - offset

    def _cons(self):
        cons = []

        for conf in self._configurations_manager.get_configurations:
            cons.append(
                {
                    'type': 'eq' if conf.resource.exact_amount else 'ineq',
                    'fun': (lambda x, conf=conf: self._generic_con(x, conf))
                }
            )

        cons.append(
            {
                'type': 'ineq',
                'fun': self._extra_conf
            }
        )

        print(cons)

        return cons

    def _extra_conf(self, x):
        sum = 30
        for i in range(3):
            sum -= x[i]

        return sum


    def _bounds(self):
        return [(0, None)] * len(self._configurations_manager.get_configurations[0].sections)

    # this implementation is for weird round behaviour,
    # sometimes 6.00000000e+03 -> 6000, but in some situations 6.00000000e+03 -> 5999
    def _custom_ceil(self, x: float) -> int:
        return math.ceil(float("{0:.2f}".format(x)))
