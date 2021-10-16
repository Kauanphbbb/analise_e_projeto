import unittest
from FederativeUnit import FederativeUnit


class TestFederativeUnit(unittest.TestCase):
    def setUp(self):
        self.unit = FederativeUnit('Piauí', 'Nordeste', 'PI')

    def testIsNorthwest(self):
        expected = 'Nordestino é um povo arretado'
        result = self.unit.isRegionNorthwest()
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
