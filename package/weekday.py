import datetime
def is_weekend(d :datetime.date):
    weekday: int = d.weekday()
    return weekday == 5 or weekday == 6
