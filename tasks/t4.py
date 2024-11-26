from utils import read_file
from constants import months


def unique_events_in_files():
    events = set()
    for year in range(2004, 2017, 1):
        for month in months:
            file_path = 'weatherfiles/Murree_weather_' + \
                str(year)+'_'+month+'.txt'
            file_content = read_file(file_path)
            if 'Error:' not in file_content:
                data = file_content[1:]
                for row in data:
                    if row[-2] != "":
                        events.add(row[-2])

    return events


unique_events_in_files()
