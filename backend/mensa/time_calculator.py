import datetime
from datetime import date,  timedelta
from datetime import datetime as dt
import calendar



def calculate_days():

    current_day = dt.today().strftime('%Y-%m-%d')
    today = date.fromisoformat(current_day)
    #print(today)
    dates = [today + datetime.timedelta(days=i) for i in range(0 - today.weekday(), 7 - today.weekday())]
    dates_as_string = []
    for i in range(7):
        date_item = dates[i].strftime('%Y-%m-%d')
        dates_as_string.append(date_item)

    return dates_as_string