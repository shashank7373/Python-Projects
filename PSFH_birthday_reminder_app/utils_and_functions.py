"""
    A module full of functions required for the main app and
    pytest module is written here. Some of the code is repetative
    as i have written two different programs for the app and the
    pytest program.

"""


from calendar import monthrange
from datetime import date


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


def display_birthday(birthobj):
    bday = birthobj.date().day
    bmon = birthobj.strftime("%B")
    bwday = get_weekday(birthobj)
    return f"on {bwday}, {bday}th of {bmon}"


def display_date(dateobgj):
    return dateobgj.strftime("%d-%b-%Y")


def modify_month(dateobgj, val):
    if val == 1:
        mon = dateobgj.month
        yr = dateobgj.year + mon // 12
        mon = mon % 12 + 1
        day_ = min(dateobgj.day, monthrange(yr, mon)[1])
        return date(yr, mon, day_)
    else:
        mon = dateobgj.month
        yr = dateobgj.year + mon // 12
        mon = mon % 12 - 1
        day_ = min(dateobgj.day, monthrange(yr, mon)[1])
        return date(yr, mon, day_)


def get_difference(dateobgj, birthobj):
    difference = birthobj.date() - dateobgj.date()
    return difference.days


def get_difference_test(ddate, bdate):
    difference = bdate - ddate
    return difference.days


"""
    The following three functions all have the same functionality
    of returning the remaining days string to the main app for
    different test cases.
"""


def get_birthday_status(val):
    if val == 1:
        return "Last month"
    else:
        return "Next month"


def difference_months(dateobgj, birthobj):
    diff = birthobj.date().month - dateobgj.date().month
    if diff > 0:
        if diff == 1:
            return f"Next month"
        else:
            return f"{str(diff)} months from now"
    else:
        if diff == -1:
            return f"Last month"
        else:
            return f"{str(diff)[1:]} months ago"


def calculate(difference, weekday):
    if difference == 0:
        return "Today"
    elif difference > 0:
        weeks = difference // 7
        days = difference % 7
        if difference >= 28:
            return f"{str(difference)} days from now"
        else:
            if weeks > 1 and not days:
                return f"{str(weeks)} weeks from now"
            elif weeks == 3 and days:
                return f"After {str(weeks)} weeks"
            elif weeks > 1 and days:
                return f"{str(difference)} days from now"
            elif weeks == 1:
                return f"Next {str(weekday)}"
            elif days > 2:
                return f"Coming {str(weekday)}"
            elif days == 2:
                return "Day after Tomorrow"
            else:
                return "Tomorrow"
    else:
        difference_pos = abs(difference)
        weeks = difference_pos // 7
        days = difference_pos % 7
        if difference_pos >= 28:
            return "Almost a month ago"
        else:
            if weeks >= 2:
                return f"{str(weeks)} weeks ago"
            elif weeks == 1 and days:
                return "in the last week"
            elif weeks == 1:
                return f"Last {str(weekday)}"
            elif days > 2:
                return f"{str(difference_pos)} days back"
            elif days == 2:
                return "Day before Yesterday"
            else:
                return "Yesterday"
