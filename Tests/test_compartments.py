# Copyright (c) 2020, Build-A-Cell. All rights reserved.
# See LICENSE file in the project root directory for details.

from unittest import TestCase
from biocrnpyler import Species, Compartment
import pytest


class TestSpecies(TestCase):

    def test_compartment_initialization(self):
        # tests naming convention repr without species type or attributes
        species = Species(name='test_species')
        compartment = Compartment(name='test_compartment')
        species.compartment = compartment
        self.assertEqual(compartment.name, 'test_compartment')
        self.assertEqual(species.compartment.name, compartment.name)

        # tests naming convention for species with name and compartment
        compartment = Compartment(name='test_compartment', spatial_dimensions = 1, volume = 1e-4)
        self.assertEqual(compartment.spatial_dimensions, 1)
        self.assertEqual(compartment.volume, 1e-4)
        with pytest.raises(ValueError):
            Compartment(name='2test_compartment')

        with pytest.raises(ValueError, match = 'Compartment name must be a string'):
            compartment = Compartment(name = "test_compartment")
            compartment.name = 24

        with pytest.raises(ValueError, match = 'Compartment volume must be a float.'):
            Compartment(name = "test_compartment", volume= '2.5')

        with pytest.raises(ValueError, match = 'Compartment volume must be non-negative.'):
            Compartment(name = "test_compartment", volume= -2)

        with pytest.raises(ValueError, match = 'Compartment spatial dimension must be an integer.'):
            Compartment(name = "test_compartment", spatial_dimensions= 2.5)

        with pytest.raises(ValueError, match = 'Compartment spatial dimension must be non-negative.'):
            Compartment(name = "test_compartment", spatial_dimensions= -2)

        with pytest.raises(ValueError, match = 'Compartments with same names must have the same volume and spatial dimensions.'):
            compartment1 = Compartment(name = "test_compartment", spatial_dimensions= 2)
            compartment2 = Compartment(name = "test_compartment", spatial_dimensions= 3)
            self.assertEqual(compartment1, compartment2)