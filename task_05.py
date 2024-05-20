import datetime as dt


def date_in_future(integer=0):
    time_now = dt.datetime.now()
    if not isinstance(integer, int) or not str(integer).isdigit():
        return time_now.strftime('%d-%m-%Y %H:%M:%S')

    day_delta = time_now + dt.timedelta(days=integer)
    return day_delta.strftime('%d-%m-%Y %H:%M:%S')
