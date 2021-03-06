from days_of_week import DayOfWeek
from months import Month

class GregorianDate:
    
    def __init__(self, year, month, day):
        assert self._is_valid_gregorian(year, month, day), \
                "Invalid Gregorian date."
                
        self.year = year
        self.month = month
        self.day = day
        
        
    def is_leap_year(self):
        return GregorianDate._is_leap_year(self.year)
    
    
    @staticmethod
    def _is_leap_year(year):
        if year % 400 is 0:
            return True
        
        if (year % 4 is 0) and (year % 100 is not 0):
            return True
         
        return False
    
    
    @staticmethod
    def _month_days(year, month):
        max_month_days = {1  : 31,
                          2  : 29 if GregorianDate._is_leap_year(year) else 28,
                          3  : 31,
                          4  : 30,
                          5  : 31,
                          6  : 30,
                          7  : 31,
                          8  : 31,
                          9  : 30,
                          10 : 31,
                          11 : 30,
                          12 : 31}
        
        return max_month_days[month]
    
    
    def month_days(self):
        return GregorianDate._month_days(self.year, self.month)
    
    
    @staticmethod
    def _is_valid_gregorian(year, month, day):
        if year is 4713 and month < 11:
            return False
            
        if year is 4713 and month is 11 and day < 15:
            return False
        
        if month > 12:
            return False
        
        if day > GregorianDate._month_days(year, month):
            return False
        
        return True
        
        
    def to_julian(self):
        return GregorianDate._to_julian(self.year, self.month, self.day)
    
    
    @staticmethod
    def _to_julian(year, month, day):
        if month < 3:
            year -= 1
            month += 12
 
        A = year // 100
        B = A // 4
        C = 2 - A + B
        E = 365.25 * (year + 4716)
        F = 30.6001 * (month + 1)
        
        return int(C + day + E + F -1524.5) 
    
    
    def month_name(self):
        return Month(self.month).name
    
    
    def day_of_week_name(self):
        return DayOfWeek(self.day_of_week()).name
    
    
    def day_of_week(self):
        return GregorianDate._day_of_week(self.year, self.month, self.day)
    
                 
    @staticmethod
    def _day_of_week(year, month, day):
        if  month < 3 :
            month = month + 12
            year = year - 1
            
        return  (((13 * month + 3) // 5 + day + \
                 year + year // 4 - year // 100 + year // 400) + 1) % 7
                 

    def print_month(self):
        width = 26
        s = "         Calendar         "
        s += "Su  Mo  Tu  We  Th  Fr  Sa"
        s += format()
        for i in range(2, self.month_days()):
            s += ' '
    
    
    def __eq__(self, other_date):
        return (self.year, self.month, self.day) == (other_date.year, other_date.month, other_date.day)
    
    
    def __str__(self):
        return str(self.year) + '-' + str(self.month) + '-' + str(self.day)