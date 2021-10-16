import unittest
from Employer import Employer


class TestEmployer(unittest.TestCase):
    def setUp(self):
        self.unit = Employer('Kauan', '123.456.789-01',
                             '03/10/2001', '1298741', True, 600, 'estagiário')

    def testAttributes(self):
        expected = 600
        result = self.unit.monthlyIncome
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
