from utils import read_file
from constants import months


def rain_event_in_months():
    rain_months = []
    for year in range(2004, 2017, 1):
        for month in months:
            file_path = 'weatherfiles/Murree_weather_' + \
                str(year)+'_'+month+'.txt'
            file_content = read_file(file_path)
            if 'Error:' not in file_content:
                data = file_content[1:]
                for row in data:
                    if row[-2] != "" and 'Rain' == row[-2]:
                        date = row[0].split('-')
                        rain_months.append(date[1])

    return rain_months


rain_event_in_months()
