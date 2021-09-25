import datetime
def is_weekend(today :datetime.date):
    weekday: int = today.weekday()
    return weekday == 5 or weekday == 6
