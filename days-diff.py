from datetime import datetime


def days_diff(date1, date2):
    d1, d2 = sorted((datetime(*date1), datetime(*date2)))
    return (d2 - d1).days
