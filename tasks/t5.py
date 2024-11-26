from utils import get_all_files_contents


def get_rain_event_in_months():
    rain_months = []
    data = get_all_files_contents()
    for row in data:
        if row[-2] != "" and 'Rain' == row[-2]:
            date = row[0].split('-')
            rain_months.append(date[1])
    return rain_months


get_rain_event_in_months()
