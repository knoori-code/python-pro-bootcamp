def is_leap_year(year):
    """States whether input year is a leap year"""
    if year % 400 == 0:
        return True
    
    if year % 100 == 0:
        return False
    
    if year % 4 == 0:
        return True
    
    return False

print(is_leap_year(2100))