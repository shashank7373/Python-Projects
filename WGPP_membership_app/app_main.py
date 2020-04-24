"""
    A main function which return a tuple of stings to be displayed
    on the app. The birthstring is pre set in this program as well.
    The main code is written "in basic_app_design.py".
"""


from datetime import datetime
from utils_and_functions import *


def main_func(datestr):
    # Change renewstr to "15/01/2020" run "test_cases_jan.txt" file
    # renewstr = "15/01/2020"
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
        return (" ", display_date(dtobj), wday, get_renewal_status(), display_renewal(dtobj, rnobj))
    else:
        if diff == 0:
            return ("Renewal Day", display_date(dtobj), wday, calculate(diff, rwday), display_renewal(dtobj, rnobj))
        elif (diff != 0) and (lastDiff <= diff <= 30):
            return (" ", display_date(dtobj), wday, calculate(diff, rwday), display_renewal(dtobj, rnobj))
        else:
            return (" ", display_date(dtobj), wday, difference_months(dtobj, rnobj), display_renewal(dtobj, rnobj))
