"""
    A module full of functions required for the main app and
    pytest module is written here. Some of the code is repetative
    as i have written two different programs for the app and the
    pytest program.

"""


from calendar import monthrange
from datetime import datetime
from datetime import timedelta
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
        if mon != 12:
            mon = mon + 1
        else:
            mon = 1
        day_ = min(dateobgj.day, monthrange(yr, mon)[1])
        return date(yr, mon, day_)
    else:
        mon = dateobgj.month
        yr = dateobgj.year
        if mon != 1:
            mon = mon - 1
        else:
            yr = yr - 1
            mon = 12
        day_ = min(dateobgj.day, monthrange(yr, mon)[1])
        return date(yr, mon, day_)


def get_difference(dateobgj, birthobj):
    difference = birthobj.date() - dateobgj.date()
    return difference.days


def get_difference_test(ddate, bdate):
    difference = bdate - ddate
    return difference.days


def add_date(dateobgj, diff):
    return dateobgj + timedelta(days = diff)


def sub_date(dateobgj, diff):
    return dateobgj - timedelta(days = diff)


def get_first_date_of_month(dateobgj):
    present = get_day(dateobgj)
    first_date = sub_date(dateobgj, present-1)
    return first_date


def get_last_date_of_month(dateobgj):
    present = get_day(dateobgj)
    delta = 32 if present <= 12 else 16
    next_month = add_date(dateobgj, delta)

    next_month_first = get_first_date_of_month(next_month)
    last_date = sub_date(next_month_first, 1)
    return last_date


def check_valid_date(datestr):
    date_li = datestr.split("/")
    dd, mm, yyyy = list(map(int, date_li))
    try:
        date(yyyy, mm, dd)
        return True
    except ValueError:
        return False


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


def date_set_generator(birthstr):
    birth_list = birthstr.split(r'/')
    dd, mm, yyyy = list(map(int, birth_list))
    birthobj = datetime(yyyy, mm, dd)

    with open(r"dataset.txt", 'w') as FH:
        FH.write("Date\n")

        for month in range(1, 13):
            if month in range(mm-1, mm+2):
                # dates 15 days below and beyond birthstr
                if month == mm:
                    present_date_minus_15 = sub_date(birthobj, 15)
                    present_date_plus_15 = add_date(birthobj, 15)
                    i = 0
                    while True:
                        i += 1
                        write_date = add_date(present_date_minus_15, i)
                        if write_date == present_date_plus_15:
                            break
                        FH.write(write_date.strftime("%d/%m/%Y") + "\n")

                elif month == mm-1:
                    date_of_month = datetime(yyyy, month, dd)
                    first_day = get_first_date_of_month(date_of_month)
                    FH.write(first_day.strftime("%d/%m/%Y") + "\n")
                    middle_day = date(yyyy, month, 12)
                    FH.write(middle_day.strftime("%d/%m/%Y") + "\n")

                elif month == mm+1:
                    date_of_month = datetime(yyyy, month, dd)
                    middle_day = date(yyyy, month, 18)
                    FH.write(middle_day.strftime("%d/%m/%Y") + "\n")
                    last_day = get_last_date_of_month(date_of_month)
                    FH.write(last_day.strftime("%d/%m/%Y") + "\n")

            else:
                # 1st and last dates of months
                date_of_month = datetime(yyyy, month, dd)
                first_day = get_first_date_of_month(date_of_month)
                FH.write(first_day.strftime("%d/%m/%Y") + "\n")
                last_day = get_last_date_of_month(date_of_month)
                FH.write(last_day.strftime("%d/%m/%Y") + "\n")


"""
    A main function which return a tuple of stings to be displayed
    on the app.
"""


def main_func(datestr, birthstr):
    btobj = datetime.strptime(birthstr, "%d/%m/%Y")
    dtobj = datetime.strptime(datestr, "%d/%m/%Y")
    
    lmonthDate = modify_month(btobj, -1)
    nmonthDate = modify_month(btobj, 1)

    wday = get_weekday(dtobj)
    bwday = get_weekday(btobj)

    diff = get_difference(dtobj, btobj)
    try:
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
    except Exception as e:
        print(e)
