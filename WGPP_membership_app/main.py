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
    renewstr = sys.argv[2]
    renewstr = renewstr[:-4] + "2020"
except IndexError:
    datestr = "12/12/2020"
    renewstr = "15/03/2020"

rnobj = datetime.strptime(renewstr, "%d/%m/%Y")
dtobj = datetime.strptime(datestr, "%d/%m/%Y")

lmonthDate = modify_month(rnobj)
lastDate = get_last_date_of_month(rnobj)

wday = get_weekday(dtobj)
rwday = get_weekday(rnobj)

diff = get_difference(dtobj, rnobj)
lastDiff = get_difference(lastDate, rnobj)
if dtobj.date() == lmonthDate:
    print(
        f"         || {display_date(dtobj)} || {wday} || {get_renewal_status()} || {display_renewal(dtobj, rnobj)}")
else:
    if diff == 0:
        print(
            f"Renewal Day || {display_date(dtobj)} || {wday} || {calculate(diff, rwday)} || {display_renewal(dtobj, rnobj)}")
    elif (diff != 0) and (lastDiff <= diff <= 30):
        print(
            f"         || {display_date(dtobj)} || {wday} || {calculate(diff, rwday)} || {display_renewal(dtobj, rnobj)}")
    else:
        print(
            f"         || {display_date(dtobj)} || {wday} || {difference_months(dtobj, rnobj)} || {display_renewal(dtobj, rnobj)}")
