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
    birthstr = "15/03/2020"

    btobj = datetime.strptime(birthstr, "%d/%m/%Y")
    dtobj = datetime.strptime(datestr, "%d/%m/%Y")

    bwday = get_weekday(btobj)
    ddate = get_date(dtobj)
    btdate = get_date(btobj)

    lmonthDate = modify_month(btobj, -1)
    nmonthDate = modify_month(btobj, 1)

    diff = get_difference_test(ddate, btdate)
    if ddate == lmonthDate:
        return get_birthday_status(-1)
    elif ddate == nmonthDate:
        return get_birthday_status(1)
    else:
        if (-30 <= diff <= 30):
            return calculate(diff, bwday)
        else:
            return difference_months(dtobj, btobj)


with open("birthday_cases.txt") as FH:
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
