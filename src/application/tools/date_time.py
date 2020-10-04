# coding: utf-8

import datetime, re


def datetime_convert(time):
    """
    Convert time to YYYYY-MM-DD HH:MM:SS
    """
    _time = str(time)
    retime = re.compile(r'\W+')
    _list = retime.split(_time)

    if len(_list) >= 6:
        year = int(_list[0])
        mounth = int(_list[1])
        day = int(_list[2])
        hour = int(_list[3])
        minute = int(_list[4])
        second = int(_list[5])
        time = datetime.datetime(year, mounth, day, hour, minute, second)
        return time

    else:
        try:
            hour = int(_list[0])
            minute = int(_list[1])
            second = int(_list[2])
            time = datetime.datetime(100, 1, 1, hour, minute, second)
            return time

        except IndexError:
            hour = int(_list[0])
            minute = int(_list[1])
            time = datetime.datetime(hour, minute)
            return time


def date_convert(date):
    """
    Convert str date to python format: YYYY-MM-DD
    """
    _date = str(date)
    redate = re.compile(r'\W+')
    _list = redate.split(_date)
    try:
        day = int(_list[0])
        mounth = int(_list[1])
        year = int(_list[2])
        date = datetime.date(year, mounth, day)
        return date
    except ValueError:
        day = int(_list[2])
        mounth = int(_list[1])
        year = int(_list[0])
        date = datetime.date(year, mounth, day)
        return date


def time_convert(time):
    """
    Convert time to HH:MM:SS
    """
    _time = str(time)
    retime = re.compile(r'\W+')
    _list = retime.split(_time)
    try:
        hour = int(_list[0])
        minute = int(_list[1])
        second = int(_list[2])
        time = datetime.time(hour, minute, second)
        return time
    except IndexError:
        hour = int(_list[0])
        minute = int(_list[1])
        time = datetime.time(hour, minute)
        return time


def convert_in_second(time):
    if time:
        _time = str(time)
        retime = re.compile(r'\W+')
        _list = retime.split(_time)
        try:
            hour = int(_list[0]) * 3600
            minute = int(_list[1]) * 60
            second = int(_list[2])
            time = hour + minute + second
            return time
        except IndexError:
            hour = int(_list[0]) * 3600
            minute = int(_list[1]) * 60
            time = hour + minute
            return time
    else:
        time = 0
        return time


def add_time(time, retard):
    """
    Add time to the current time
    """
    time = datetime_convert(time)
    if retard:
        _time = str(retard)
        retime = re.compile(r'\W+')
        _list = retime.split(_time)
        hour = int(_list[0]) * 3600
        minute = int(_list[1]) * 60
        time2 = hour + minute
        new_time = time + datetime.timedelta(0, time2)
    else:
        new_time = time
    return new_time.time()


def remove_time(time, retard):
    time = datetime_convert(time)
    if retard:
        _time = str(retard)
        retime = re.compile(r'\W+')
        _list = retime.split(_time)
        hour = int(_list[0]) * 3600
        minute = int(_list[1]) * 60
        time2 = hour + minute
        new_time = time - datetime.timedelta(0, time2)
    else:
        new_time = time
    return new_time.time()


def format_date(date, format=None):
    """
    Format date
    """
    newdate = date.strftime(format)
    return newdate
