import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = Location("SLO", 35.3, -120.7)
        loc4 = loc1
        self.assertEqual(repr(loc1),"Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc2),"Location('Paris', 48.9, 2.4)")
        self.assertEqual(repr(loc3),"Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc4),"Location('SLO', 35.3, -120.7)")

    # Add more tests!

    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = Location("SLO", 35.3, -120.7)
        loc4 = loc1
        self.assertEqual(Location.__eq__(loc1, loc3), True)
        self.assertEqual(Location.__eq__(loc1, loc4), True)
        self.assertEqual(Location.__eq__(loc1, loc2), False)
        self.assertEqual(Location.__eq__(loc4, loc2), False)

if __name__ == "__main__":
        unittest.main()
