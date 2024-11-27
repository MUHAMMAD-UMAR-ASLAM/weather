from utils import get_all_files_contents
from constants import  INDEX_LOOKUP
def get_rain_event_in_months():
    rain_months = []
    data = get_all_files_contents()
    for row in data:
        if row[INDEX_LOOKUP['unique_events']] != "" and 'Rain' == row[INDEX_LOOKUP['unique_events']]:
            date = row[INDEX_LOOKUP['date']].split('-')
            rain_months.append(date[1])
    return rain_months


get_rain_event_in_months()
