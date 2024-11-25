from utils import read_file
from constants import months


def find_minimumm_temperature(year):
    min = float('inf')
    for month in months:
        file_path = 'weatherfiles/Murree_weather_'+str(year)+'_'+month+'.txt'
        file_content = read_file(file_path)
        data = file_content[1:]
        for row in data:
            if row[3] != "" and min > float(row[3]):
                min = float(row[3])

    return min


find_minimumm_temperature(2011)
