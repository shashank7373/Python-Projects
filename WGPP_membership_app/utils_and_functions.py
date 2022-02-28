"""
    A module full of functions required for the main app and
    pytest module is written here. Some of the code is repetative
    as i have written two different programs for the app and the
    pytest program.

"""


from calendar import monthrange
from datetime import date, timedelta


"""
    Write more number of functions if you want to
    execute main_backup.py and main_backup_1.py as it has the old code
    structure with get_day(), get_day(), get_month(), etc fuctions.
    These functions are not required for the new main function.
"""


def get_date(dateobgj):
    return dateobgj.date()


def get_day(dateobgj):
    return dateobgj.date().day


def get_month(dateobgj):
    return dateobgj.date().month


def get_weekday(dateobgj):
    weekday = dateobgj.strftime("%A")
    return weekday


def display_renewal(dateobj, renewobj):
    nextMonth = get_first_date_of_next_month(renewobj)
    if dateobj.date().month >= nextMonth.date().month:
        next_renewobj = increment_year(renewobj, 1)
        rday = next_renewobj.day
        rmon = next_renewobj.strftime("%B")
        rwday = get_weekday(next_renewobj)
        ryear = next_renewobj.year
        return f"on {rwday}, {rday}th of {rmon}, {ryear}"
    else:
        rday = renewobj.date().day
        rmon = renewobj.strftime("%B")
        rwday = get_weekday(renewobj)
        ryear = renewobj.date().year
        return f"on {rwday}, {rday}th of {rmon}, {ryear}"


def display_date(dateobgj):
    return dateobgj.strftime("%d-%b-%Y")


def modify_month(renewobj):
    if renewobj.date().month > 1:
        mon = renewobj.month
        yr = renewobj.year + mon // 12
        mon = mon % 12 - 1
        day_ = min(renewobj.day, monthrange(yr, mon)[1])
        return date(yr, mon, day_)



def get_difference(dateobgj, renewobj):
    difference = renewobj.date() - dateobgj.date()
    return difference.days


def get_difference_test(ddate, rdate):
    difference = rdate - ddate
    return difference.days


"""
    The following three functions all have the same functionality
    of returning the remaining days string to the main app for
    different test cases.
"""


def get_renewal_status():
    return "Your WGPP Annual Membership due date is next month"


def difference_months(dateobgj, renewobj):
    diff = renewobj.date().month - dateobgj.date().month
    if diff > 0:
        if diff == 1:
            return f"Your WGPP Annual Membership due date is next month"
        else:
            return f"Your WGPP Annual Membership due date is {str(diff)} months from now"
    else:
        nextRenew = increment_year(renewobj, 1)
        curRenew = get_date(dateobgj)
        noMonths = ((nextRenew.year - curRenew.year) * 12) + (nextRenew.month - curRenew.month)
        if noMonths > 10:
            return "Your WGPP Annual Membership due date is almost a year from now"
        elif noMonths == 1:
            return f"Your WGPP Annual Membership due date is almost a month from now"
        else:
            return f"Your WGPP Annual Membership due date is almost {str(noMonths)} months from now"


def calculate(difference, weekday):
    if difference == 0:
        return "Your WGPP Annual Membership due date is Today"
    elif difference > 0:
        weeks = difference // 7
        days = difference % 7
        if difference >= 28:
            return f"Your WGPP Annual Membership due date is {str(difference)} days from now"
        else:
            if weeks > 1 and not days:
                return f"Your WGPP Annual Membership due date is {str(weeks)} weeks from now"
            elif weeks == 3 and days:
                return f"Your WGPP Annual Membership due date is after {str(weeks)} weeks"
            elif weeks > 1 and days:
                return f"Your WGPP Annual Membership due date is {str(difference)} days from now"
            elif weeks == 1:
                return f"Your WGPP Annual Membership due date is next {str(weekday)}"
            elif days > 2:
                return f"Your WGPP Annual Membership due date is coming {str(weekday)}"
            elif days == 2:
                return "Your WGPP Annual Membership due date is day after Tomorrow"
            else:
                return "Your WGPP Annual Membership due date is Tomorrow"
    else:
        difference_pos = abs(difference)
        weeks = difference_pos // 7
        days = difference_pos % 7
        if difference_pos >= 28:
            return "Almost a month ago"
        else:
            if weeks >= 2:
                return f"Your WGPP Annual Membership due date was {str(weeks)} weeks ago"
            elif weeks == 1 and days:
                return "Your WGPP Annual Membership due date was in the last week"
            elif weeks == 1:
                return f"Your WGPP Annual Membership due date was last {str(weekday)}"
            elif days > 2:
                return f"Your WGPP Annual Membership due date was {str(difference_pos)} days back"
            elif days == 2:
                return "Your WGPP Annual Membership due date was day before Yesterday"
            else:
                return "Your WGPP Annual Membership due date was Yesterday"


"""
    New functions written for the new requirements of WGPP app.
"""


def add_date(dateobgj, diff):
    return dateobgj + timedelta(days=diff)


def sub_date(dateobgj, diff):
    return dateobgj - timedelta(days=diff)


def get_first_date_of_month(dateobgj):
    present = get_day(dateobgj)
    first_date = sub_date(dateobgj, present-1)
    return first_date


def get_first_date_of_next_month(renewobj):
    present = get_day(renewobj)
    val = 32 if present <=15 else 16
    next_month = add_date(renewobj, val)
    next_month_first = get_first_date_of_month(next_month)
    return next_month_first


def get_last_date_of_month(renewobj):
    present = get_day(renewobj)
    val = 32 if present <= 15 else 16
    next_month = add_date(renewobj, val)

    next_month_first = get_first_date_of_month(next_month)
    last_date = sub_date(next_month_first, 1)
    return last_date


def increment_year(renewobj, years):
    renewDate = get_date(renewobj)
    try:
        return renewDate.replace(year = renewDate.year + years)
    except ValueError:
        return renewDate + (date(renewDate.year + years, 1, 1) - date(renewDate.year, 1, 1))

