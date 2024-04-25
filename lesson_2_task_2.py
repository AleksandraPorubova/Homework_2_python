def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

result = is_year_leap(2001)
print("Год 2001: ", result)