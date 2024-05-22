import unittest
import datetime
from main import lpn, is_master, lucky_color, compare_lpn, get_gen

class TestNumerology(unittest.TestCase):

    def test_lpn(self):
        self.assertEqual(lpn(datetime.date(1990, 4, 15)), 11)  
        self.assertEqual(lpn(datetime.date(1985, 12, 30)), 11)  
        self.assertEqual(lpn(datetime.date(2000, 1, 1)), 4)
        self.assertEqual(lpn(datetime.date(2011, 11, 11)), 8)
        self.assertEqual(lpn(datetime.date(2020, 3, 14)), 3) 
        self.assertEqual(lpn(datetime.date(1988, 8, 8)), 6)

    def test_is_master(self):
        self.assertTrue(is_master(11))
        self.assertTrue(is_master(22))
        self.assertTrue(is_master(33))
        self.assertFalse(is_master(4))
        self.assertFalse(is_master(9))

    def test_lucky_color(self):
        self.assertEqual(lucky_color(1), "Red")
        self.assertEqual(lucky_color(2), "Orange")
        self.assertEqual(lucky_color(3), "Yellow")
        self.assertEqual(lucky_color(4), "Green")
        self.assertEqual(lucky_color(5), "Blue")
        self.assertEqual(lucky_color(6), "Indigo")
        self.assertEqual(lucky_color(7), "Violet")
        self.assertEqual(lucky_color(8), "Purple")
        self.assertEqual(lucky_color(9), "Gold")
        self.assertEqual(lucky_color(11), "Silver")
        self.assertEqual(lucky_color(22), "Platinum")
        self.assertEqual(lucky_color(33), "Diamond")
        self.assertEqual(lucky_color(99), "Unknown")

    def test_compare_lpn(self):
        self.assertTrue(compare_lpn(datetime.date(1990, 4, 15), datetime.date(1985, 12, 30)))  
        self.assertFalse(compare_lpn(datetime.date(1990, 4, 15), datetime.date(1980, 5, 21)))
        self.assertFalse(compare_lpn(datetime.date(2000, 1, 1), datetime.date(2004, 1, 1)))  
        self.assertFalse(compare_lpn(datetime.date(2000, 1, 1), datetime.date(2000, 2, 2)))  

    def test_get_gen(self):
        self.assertEqual(get_gen(datetime.date(1925, 6, 15)), "Greatest Generation")
        self.assertEqual(get_gen(datetime.date(1930, 6, 15)), "Silent Generation")
        self.assertEqual(get_gen(datetime.date(1950, 6, 15)), "Baby Boomers")
        self.assertEqual(get_gen(datetime.date(1975, 6, 15)), "Generation X")
        self.assertEqual(get_gen(datetime.date(1990, 6, 15)), "Millennials")
        self.assertEqual(get_gen(datetime.date(2000, 6, 15)), "Generation Z")
        self.assertEqual(get_gen(datetime.date(2020, 6, 15)), "Generation Alpha")
        self.assertEqual(get_gen(datetime.date(1900, 6, 15)), "Unknown Generation")
        self.assertEqual(get_gen(datetime.date(2025, 6, 15)), "Unknown Generation")

if __name__ == "__main__":
    unittest.main()
