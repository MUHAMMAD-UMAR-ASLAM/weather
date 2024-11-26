import csv
from constants import  months

def get_file_content(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            rows = []
            for row in reader:
                rows.append(row)
            return rows
    except FileNotFoundError:
        return None


def get_file_contents_by_year(year):
    files = []
    for month in months:
        file_path = 'weatherfiles/Murree_weather_' + str(year)+ '_'+month+'.txt'
        file_content = get_file_content(file_path)
        if file_content:
            files.append(file_content[1:])
    return  files


def get_all_files_contents():
    files = []
    for year in range(2004, 2017, 1):
        for month in months:
            file_path = 'weatherfiles/Murree_weather_' + \
                        str(year) + '_' + month + '.txt'
            file_content = get_file_content(file_path)
            if file_content:
                files.append(file_content[1:])
    return files
