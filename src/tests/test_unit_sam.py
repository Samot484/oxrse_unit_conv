import unittest
from oxrse_unit_conv.units import m2, sam


class TestSam(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(sam.si_unit.matches(m2))

    def test_basic_conversion(self):
        self.assertEqual(sam.to_si(1), 8565.32)
        self.assertEqual(sam.to_unit(10, sam), 10)


if __name__ == '__main__':
    unittest.main()
