"""
    A pytest program to test all the test cases.
    It takes input date strings and expected output,
    and varifies all test cases for a birth string which is
    pre set inside the program.
"""

import pytest
from datetime import datetime
from utils_and_functions import *


def main_validate(datestr):
    # Change renewstr to run "test_cases_jan.txt" file
    # renewstr = "15/01/2020"
    renewstr = "15/03/2020"

    rnobj = datetime.strptime(renewstr, "%d/%m/%Y")
    dtobj = datetime.strptime(datestr, "%d/%m/%Y")

    rwday = get_weekday(rnobj)
    ddate = get_date(dtobj)
    rndate = get_date(rnobj)

    lmonthDate = modify_month(rnobj)
    lastDate = get_last_date_of_month(rnobj)

    diff = get_difference_test(ddate, rndate)
    lastDiff = get_difference(lastDate, rnobj)
    if ddate == lmonthDate:
        return get_renewal_status()
    else:
        if (lastDiff <= diff <= 30):
            return calculate(diff, rwday)
        else:
            return difference_months(dtobj, rnobj)

"""
    Change the file to "test_cases_jan.txt" to run for
    "15/01/2020" renewal date.
"""
with open("test_cases_mar.txt") as FH:
    header = next(FH)
    all_lines = list()
    for line in FH:
        date, remaining_days = line.split(",")
        all_lines.append((date, remaining_days.split("\n")[0]))

# print(len(all_lines))


@pytest.mark.parametrize('ndate, remaining', all_lines)
def test_validate(ndate, remaining):
    exp = main_validate(ndate)
    assert remaining == exp
