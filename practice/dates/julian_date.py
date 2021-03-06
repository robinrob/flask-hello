from gregorian_date import GregorianDate

class JulianDate:
    
    def __init__(self, julian_day):
        self.julian_day = julian_day
    
    
    def to_gregorian(self):
        return JulianDate._to_gregorian(self.julian_day)
    
    
    @staticmethod
    def _to_gregorian(julian_day):
        A = julian_day + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        
        return GregorianDate(int(year), int(month), int(day))
    
    
    def day_of_week(self):
        return (self.julian_day + 1) % 7 
    
    
    def __lt__(self, other_date):
        return self.julian_day < other_date.julian_day


    def __le__(self, other_date):
        return self.julian_day <= other_date.julian_day