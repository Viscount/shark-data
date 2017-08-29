#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import *
from dateutil.rrule import rrule, MONTHLY



class Month:
    def __init__(self, date_time):
        self.year = date_time.year
        self.month = date_time.month
        self.name = str(self.year) + "." + str(self.month)
        self.start_date = date_time


def get_between_month(start_date):
    month_list = []
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    if start_date > datetime.now():
        start_date = datetime.now()
    datetime_list = list(rrule(freq=MONTHLY, dtstart=start_date, until=datetime.now()))
    for date_time in datetime_list:
        month_list.append(Month(date_time))
    return month_list


if __name__ == "__main__":
    month_list = get_between_month("2016-07-01")
    print len(month_list)
