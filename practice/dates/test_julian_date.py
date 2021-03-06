import unittest
from julian_date import JulianDate
from julian_date import GregorianDate

class TestJulianDate(unittest.TestCase):

    def Test_should_convert_to_gregorian(self):
        date = JulianDate(2446971)
        
        self.assertTrue(GregorianDate(1987, 6, 24) == date.to_gregorian())
        
    
    def Test_should_return_1_for_day_of_week(self):
        date = JulianDate(0)
        
        self.assertEqual(1, date.day_of_week())
        
        
    def Test_should_return_3_for_day_of_week(self):
        date = JulianDate(2446971)
        
        self.assertEqual(3, date.day_of_week())
        
        
    def Test_should_return_0_for_day_of_week(self):
        date = JulianDate(2455928)
        
        self.assertEqual(0, date.day_of_week())
