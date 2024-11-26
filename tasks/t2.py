from utils import read_file
from constants import months


def find_minimumm_temperature(year):
    max_value = float('-inf')
    for month in months:
        file_path = 'weatherfiles/Murree_weather_'+str(year)+'_'+month+'.txt'
        file_content = read_file(file_path)
        data = file_content[1:]
        for row in data:
            if row[1] != "" and max_value < float(row[1]):
                max_value = float(row[1])

    return max_value


find_minimumm_temperature(2011)
