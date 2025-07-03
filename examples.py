import math

def ordinal_indicator(year):
    """ determines what ordinal indicator to return to calling function based on year provided. Also checks edge case for teen years which follow unique rules."""

    teen_year_check = year % 100
    if 10 <= teen_year_check <= 19:
        return "th"
    
    match year % 10:
        case 0:
            return "th"
        case 1:
            return "st"
        case 2:
            return "nd"
        case 3:
            return "rd"
        case _:
            return "th"

def century(year):
    """takes a year as input and returns the century associated with that year. Also adds an ordinal indicator e.g. 20th or 21st."""
    year = math.ceil(year / 100)
    result = str(year) + ordinal_indicator(year)
    return result


print(century(1))