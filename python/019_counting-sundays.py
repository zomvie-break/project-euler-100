#!/usr/bin/env python3

def run():
    '''
    returns the number of sundays since 1901/01/01 to 2000/12/31
    '''
    # dictionary that stores the months' number from 0..11 with the number of days as value
    months_dir= {0:31, 1:28, 2:31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31, 10:30, 11:31}
    # list that stores the number of days of each weekday, mostly for debugging purposes
    days = [0]*7
    # flag used to identify
    flag = 0
    # variable that stores the number of sundays
    sundays_first_day = 0

    # for loop, 1900..2000
    for year in range(1900,2001):
        if year % 4 == 0:       # check if the year should be a leap year
            # if the year is divisible by 100 (to check for century)
            # and not divisible by 400, it is not a leap year
            if year % 100 == 0 and year % 400 != 0:
                months_dir[1] = 28
            else:
                months_dir[1] = 29
        else:
            months_dir[1] = 28

        for month in range(12):
            for day in range(months_dir[month]):
                days[flag] += 1
                if flag == 6 and day == 0:
                    sundays_first_day += 1
                if flag == 6:
                    flag = 0
                else:
                    flag += 1
        # this deletes the count of days of the year 1900 since we are
        # only asked for the years 1901..2000 but keeps the 'flag'
        if year == 1900:
            days = [0]*7
            sundays_first_day = 0

    return sundays_first_day

print(run())
