"""
    A main function which return a tuple of stings to be displayed
    on the app. The birthstring is pre set in this program as well.
    The main code is written "in basic_app_design.py".
"""


from datetime import datetime
from utils_and_functions import *


def main_func(datestr):
    birthstr = "15/03/2020"

    btobj = datetime.strptime(birthstr, "%d/%m/%Y")
    dtobj = datetime.strptime(datestr, "%d/%m/%Y")

    lmonthDate = modify_month(btobj, -1)
    nmonthDate = modify_month(btobj, 1)

    wday = get_weekday(dtobj)
    bwday = get_weekday(btobj)

    diff = get_difference(dtobj, btobj)
    if dtobj.date() == lmonthDate:
        return (" ", display_date(dtobj), wday, get_birthday_status(-1), display_birthday(btobj))
    elif dtobj.date() == nmonthDate:
        return (" ", display_date(dtobj), wday, get_birthday_status(1), display_birthday(btobj))
    else:
        if diff == 0:
            return ("Birthday", display_date(dtobj), wday, calculate(diff, bwday), display_birthday(btobj))
        elif (diff != 0) and (-30 <= diff <= 30):
            return (" ", display_date(dtobj), wday, calculate(diff, bwday), display_birthday(btobj))
        else:
            return (" ", display_date(dtobj), wday, difference_months(dtobj, btobj), display_birthday(btobj))
