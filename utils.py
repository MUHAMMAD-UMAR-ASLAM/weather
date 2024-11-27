import csv
from constants import  MONTHS

def get_file_content(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            rows = []
            for row in reader:
                rows.append(row)
            return rows[1:]
    except FileNotFoundError:
        return None


def get_file_contents_by_year(year):
    files = []
    for month in MONTHS:
        file_path = 'weatherfiles/Murree_weather_' + str(year)+ '_' + month + '.txt'
        file_content = get_file_content(file_path)
        if file_content:
            files.append(file_content)
    return  files


def get_all_files_contents():
    files = []
    for year in range(2004, 2017, 1):
        for month in MONTHS:
            file_path = 'weatherfiles/Murree_weather_' + \
                        str(year) + '_' + month + '.txt'
            file_content = get_file_content(file_path)
            if file_content:
                files.append(file_content)
    return files
