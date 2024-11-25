from utils import read_file
from constants import months


def find_dates_with_diff():
    dates = []
    for year in range(2004, 2017, 1):
        for month in months:
            file_path = 'weatherfiles/Murree_weather_' + \
                str(year)+'_'+month+'.txt'
            file_content = read_file(file_path)
            if 'Error:' not in file_content:
                data = file_content[1:]
                for row in data:
                    if row[1] != "" and row[3] != "" and int(row[1])-int(row[3]) == 7:
                        dates.append(row[0])
    return dates


find_dates_with_diff()
