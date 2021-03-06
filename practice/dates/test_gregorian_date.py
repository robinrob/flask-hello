from unittest import TestCase

from gregorian_date import GregorianDate
from days_of_week import DayOfWeek

class TestGregorianDate(TestCase):
    
    def test_should_convert_to_julianTest(self):
        date = GregorianDate(1987, 6, 24)
        
        self.assertEqual(2446971, date.to_julian())
        
    
    def test_1987_should_not_be_leap_year(self):
        date = GregorianDate(1987, 6, 24)
        
        self.assertFalse(date.is_leap_year())
    
        
    def test_1_should_not_be_leap_year(self):
        date = GregorianDate(1, 6, 24)
        
        self.assertFalse(date.is_leap_year())
    
        
    def test_2_should_not_be_leap_year(self):
        date = GregorianDate(2, 6, 24)
        
        self.assertFalse(date.is_leap_year())
    
        
    def test_3_should_not_be_leap_year(self):
        date = GregorianDate(3, 6, 24)
        
        self.assertFalse(date.is_leap_year())
    
        
    def test_4_should_be_leap_year(self):
        date = GregorianDate(4, 6, 24)
        
        self.assertTrue(date.is_leap_year())
    
        
    def test_100_should_not_be_leap_year(self):
        date = GregorianDate(100, 6, 24)
        
        self.assertFalse(date.is_leap_year())
    
        
    def test_104_should_be_leap_year(self):
        date = GregorianDate(104, 6, 24)
        
        self.assertTrue(date.is_leap_year())
    
    
    def test_2000_should_be_leap_year(self):
        date = GregorianDate(2000, 6, 24)
        
        self.assertTrue(date.is_leap_year())
    
        
    def test_2004_should_be_leap_year(self):
        date = GregorianDate(2004, 6, 24)
        
        self.assertTrue(date.is_leap_year())

        
    def test_2008_should_be_leap_year(self):
        date = GregorianDate(2008, 6, 24)
        
        self.assertTrue(date.is_leap_year())
        
        
    def test_str_should_contain_year(self):
        date = GregorianDate(1987, 6, 24)
        
        self.assertTrue('1987' in str(date))
        
        
    def test_str_should_contain_month(self):
        date = GregorianDate(1987, 6, 24)
        
        self.assertTrue('6' in str(date))
        
        
    def test_str_should_contain_day(self):
        date = GregorianDate(1987, 6, 24)
        
        self.assertTrue('24' in str(date))
    
    
    def test_should_return_3_for_day_of_week(self):
        date = GregorianDate(1987, 6, 24)
        
        self.assertEqual(3, date.day_of_week())
        
        
    def test_should_return_0_for_day_of_week(self):
        date = GregorianDate(2012, 1, 1)
        
        self.assertEqual(0, date.day_of_week())
        
    
    def test_should_return_wednesday_for_day_of_week_name(self):
        date = GregorianDate(1987, 6, 24)
        
        self.assertEqual('Wednesday', date.day_of_week_name())
        
        
    def test_should_return_monday_for_day_of_week_name(self):
        date = GregorianDate(2012, 1, 1)
        
        self.assertEqual('Sunday', date.day_of_week_name())
        
        
    def test_should_return_june_for_month_name(self):
        date = GregorianDate(1987, 6, 24)
        
        self.assertEqual('June', date.month_name())
        
    
    def test_should_return_january_for_month_name(self):
        date = GregorianDate(2012, 1, 1)
        
        self.assertEqual('January', date.month_name())
        