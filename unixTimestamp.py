import numpy as np


def verify_input(dateData):
    #Check if month input is valid or not
    error_msg = ""
    is_error = False
    check_month = np.logical_or(dateData[:, 1] > 12, dateData[:, 1] < 1)
    if dateData[check_month, 1].size != 0:
        is_error = True
        error_msg = "Month should be in the range 1 - 12 "
    #Check if day input is valid or not
    check_day = np.logical_or(dateData[:, 2] > 31, dateData[:, 2] < 1)
    if dateData[check_day, 2].size != 0:
        is_error = True
        error_msg += "Day should be in the range 1 - 31 "
    #Check if hour input is valid or not
    check_hour = np.logical_or(dateData[:, 3] > 23, dateData[:, 3] < 0)
    if dateData[check_hour, 3].size != 0:
        is_error = True
        error_msg += "Hours should be in the range 0 - 23 "
    #Check if minutes input is valid or not
    check_min = np.logical_or(dateData[:, 4] > 59, dateData[:, 4] < 0)
    if dateData[check_min, 4].size != 0:
        is_error = True
        error_msg += "Minutes should be in the range 0 - 59 "
    #Check if seconds input is valid or not
    check_sec = np.logical_or(dateData[:, 5] > 59, dateData[:, 5] < 0)
    if dateData[check_sec, 5].size != 0:
        is_error = True
        error_msg += "Sec should be in the range 0 - 59 "
    return is_error, error_msg


def is_leap_year(year):
    """Determine whether a year is a leap year."""
    return np.logical_and(year % 4 == 0,
                          np.logical_or(year % 100 != 0, year % 400 == 0))


"""Storing number of secands before the start of the month"""
def month_dp():
    month_in_sec = {}
    thirty_one_day = 31 * 24 * 3600
    thirty_day = 30 * 24 * 3600
    month_in_sec[0] = 0
    month_in_sec[1] = thirty_one_day
    month_in_sec[2] = 28 * 24 * 3600 + month_in_sec[1]
    month_in_sec[3] = thirty_one_day + month_in_sec[2]
    month_in_sec[4] = thirty_day + month_in_sec[3]
    month_in_sec[5] = thirty_one_day + month_in_sec[4]
    month_in_sec[6] = thirty_day + month_in_sec[5]
    month_in_sec[7] = thirty_one_day + month_in_sec[6]
    month_in_sec[8] = thirty_one_day + month_in_sec[7]
    month_in_sec[9] = thirty_day + month_in_sec[8]
    month_in_sec[10] = thirty_one_day + month_in_sec[9]
    month_in_sec[11] = thirty_day + month_in_sec[10]
    return month_in_sec


def calculate_sec(dateData):
    if not type(dateData).__module__ == np.__name__:
        dateData = np.array(dateData)
    is_error, error_msg = verify_input(dateData)
    if is_error:
        raise ValueError(error_msg)

    no_of_leap_year_till_now = np.empty_like(dateData[:, 0])
    np.copyto(no_of_leap_year_till_now, dateData[:, 0])
    #Counting number of year thus far, epoch time time start from 1970 and first leap year is 1972
    gt = dateData[:, 0] > 1972
    lt = dateData[:, 0] <= 1972
    no_of_leap_year_till_now[lt] = 0
    no_of_leap_year_till_now[gt] = (
        (no_of_leap_year_till_now[gt] - 1973) / 4) + 1
    #Number of secands given the year
    years = (dateData[:, 0] - 1970
             ) * 365 * 24 * 60 * 60 + no_of_leap_year_till_now * 24 * 60 * 60
    #Segmenting the data according to the month and then accordingly adding secands
    month_sec = np.empty_like(dateData[:, 1])
    np.copyto(month_sec, dateData[:, 1])
    month_1_secs = month_sec == 1
    month_2_secs = month_sec == 2
    month_3_secs = month_sec == 3
    month_4_secs = month_sec == 4
    month_5_secs = month_sec == 5
    month_6_secs = month_sec == 6
    month_7_secs = month_sec == 7
    month_8_secs = month_sec == 8
    month_9_secs = month_sec == 9
    month_10_secs = month_sec == 10
    month_11_secs = month_sec == 11
    month_12_secs = month_sec == 12
    month_in_sec_dp = month_dp()
    month_sec[month_1_secs] = month_in_sec_dp[0]
    month_sec[month_2_secs] = month_in_sec_dp[1]
    month_sec[month_3_secs] = month_in_sec_dp[2]
    month_sec[month_4_secs] = month_in_sec_dp[3]
    month_sec[month_5_secs] = month_in_sec_dp[4]
    month_sec[month_6_secs] = month_in_sec_dp[5]
    month_sec[month_7_secs] = month_in_sec_dp[6]
    month_sec[month_8_secs] = month_in_sec_dp[7]
    month_sec[month_9_secs] = month_in_sec_dp[8]
    month_sec[month_10_secs] = month_in_sec_dp[9]
    month_sec[month_11_secs] = month_in_sec_dp[10]
    month_sec[month_12_secs] = month_in_sec_dp[11]
    #If it is a leap year and month is grearter than febrauary than we add one more day
    mask_for_leap_year = np.logical_and(
        is_leap_year(dateData[:, 0]), dateData[:, 1] > 2)
    month_sec[mask_for_leap_year] += 24 * 60 * 60

    #Adding the seconds
    output = years + month_sec + (dateData[:, 2] - 1) * 24 * 60 * 60 + (
        dateData[:, 3] * 60 * 60) + (dateData[:, 4] * 60) + dateData[:, 5]
    return output
