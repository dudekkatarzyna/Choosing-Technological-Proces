from unittest import TestCase

from cta import ResourceData
from cta.resource_configurations_manager import ResourceConfigurationsManager


class TestResourceConfigurationsManager2Resources(TestCase):
    def setUp(self):
        self.r1 = ResourceData(0.7, 2100, False)
        self.r2 = ResourceData(2.5, 1200, False)
        resource_configuration_manager = ResourceConfigurationsManager([self.r1, self.r2], 5.2)
        self.configurations = resource_configuration_manager.get_configurations

    def test_get_configurations_count(self):
        self.assertEqual(len(self.configurations), 2)

    def test_get_configurations_order(self):
        self.assertEqual(self.configurations[0].resource, self.r2)
        self.assertEqual(self.configurations[1].resource, self.r1)

    def test_get_configurations_result_size(self):
        self.assertEqual(len(self.configurations[0].sections), 3)

    def test_get_configurations_sections(self):
        self.assertEqual(self.configurations[0].sections, [2, 1, 0])
        self.assertEqual(self.configurations[1].sections, [0, 3, 7])


class TestResourceConfigurationsManager3Resources(TestCase):
    def setUp(self):
        self.r1 = ResourceData(5, 0, False)
        self.r2 = ResourceData(11, 0, False)
        self.r3 = ResourceData(8, 0, False)
        resource_configuration_manager = ResourceConfigurationsManager([self.r1, self.r2, self.r3], 30)
        self.configurations = resource_configuration_manager.get_configurations

    def test_get_configurations_count(self):
        self.assertEqual(len(self.configurations), 3)

    def test_get_configurations_order(self):
        self.assertEqual(self.configurations[0].resource, self.r2)
        self.assertEqual(self.configurations[1].resource, self.r3)
        self.assertEqual(self.configurations[2].resource, self.r1)

    def test_get_configurations_result_size(self):
        self.assertEqual(len(self.configurations[0].sections), 9)

    def test_get_configurations_sections(self):
        self.assertEqual(self.configurations[0].sections, [2, 2, 1, 1, 1, 0, 0, 0, 0])
        self.assertEqual(self.configurations[1].sections, [1, 0, 2, 1, 0, 3, 2, 1, 0])
        self.assertEqual(self.configurations[2].sections, [0, 1, 0, 2, 3, 1, 2, 4, 6])


class TestResourceConfigurationsManager4Resources(TestCase):
    def setUp(self):
        self.r1 = ResourceData(5, 0, False)
        self.r2 = ResourceData(11, 0, False)
        self.r3 = ResourceData(8, 0, False)
        self.r4 = ResourceData(2, 0, False)
        resource_configuration_manager = ResourceConfigurationsManager([self.r1, self.r2, self.r3, self.r4], 40)
        self.configurations = resource_configuration_manager.get_configurations

    def test_get_configurations_count(self):
        self.assertEqual(len(self.configurations), 4)

    def test_get_configurations_order(self):
        self.assertEqual(self.configurations[0].resource, self.r2)
        self.assertEqual(self.configurations[1].resource, self.r3)
        self.assertEqual(self.configurations[2].resource, self.r1)
        self.assertEqual(self.configurations[3].resource, self.r4)

    def test_get_configurations_result_size(self):
        self.assertEqual(len(self.configurations[0].sections), 54)

    def test_get_configurations_sections(self):
        self.assertEqual(self.configurations[0].sections,
                         [3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(self.configurations[1].sections,
                         [0, 0, 2, 1, 1, 1, 0, 0, 0, 0, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 5, 4, 4, 3, 3,
                          3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(self.configurations[2].sections,
                         [1, 0, 0, 2, 1, 0, 3, 2, 1, 0, 1, 0, 2, 1, 0, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0, 0, 1, 0, 3, 2,
                          1, 0, 4, 3, 2, 1, 0, 6, 5, 4, 3, 2, 1, 0, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        self.assertEqual(self.configurations[3].sections,
                         [1, 3, 1, 0, 2, 5, 1, 4, 6, 9, 0, 2, 1, 4, 6, 0, 3, 5, 8, 10, 2, 4, 7, 9, 12, 14, 0, 1, 4, 0,
                          3, 5, 8, 2, 4, 7, 9, 12, 1, 3, 6, 8, 11, 13, 16, 0, 2, 5, 7, 10, 12, 15, 17, 20])
