"""
By Tay King Yu, Galen, s10258811, p07
"""
year = int(input("Please enter the year: "))
if (year % 4 == 0) and (year % 100 != 0 or year %400)== 0 :
    print("{} is a leap year.".format(year))
else:
    print("{} is not a leap year.".format(year))

