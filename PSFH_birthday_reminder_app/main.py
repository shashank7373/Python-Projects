"""
    This function takes input datestring and birthday string from
    the terminal and prints a desired string of output with
    remaining days displayed.
"""


import sys
from datetime import datetime
from utils_and_functions import *


# Main starts from here
try:
    datestr = sys.argv[1]
    birthstr = sys.argv[2]
    birthstr = birthstr[:-4] + "2020"
except IndexError:
    datestr = "12/12/2020"
    birthstr = "15/03/2020"

btobj = datetime.strptime(birthstr, "%d/%m/%Y")
dtobj = datetime.strptime(datestr, "%d/%m/%Y")

lmonthDate = modify_month(btobj, -1)
nmonthDate = modify_month(btobj, 1)

wday = get_weekday(dtobj)
bwday = get_weekday(btobj)

diff = get_difference(dtobj, btobj)
if dtobj.date() == lmonthDate:
    print(
        f"         || {display_date(dtobj)} || {wday} || {get_birthday_status(-1)} || {display_birthday(btobj)}")
elif dtobj.date() == nmonthDate:
    print(
        f"         || {display_date(dtobj)} || {wday} || {get_birthday_status(1)} || {display_birthday(btobj)}")
else:
    if diff == 0:
        print(
            f"Birthday || {display_date(dtobj)} || {wday} || {calculate(diff, bwday)} || {display_birthday(btobj)}")
    elif (diff != 0) and (-30 <= diff <= 30):
        print(
            f"         || {display_date(dtobj)} || {wday} || {calculate(diff, bwday)} || {display_birthday(btobj)}")
    else:
        print(
            f"         || {display_date(dtobj)} || {wday} || {difference_months(dtobj, btobj)} || {display_birthday(btobj)}")
